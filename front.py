import httpx
from pywebio.session import set_env
from pywebio.input import input, TEXT, textarea, file_upload
from pywebio.output import put_text, put_html, put_markdown, clear, put_loading, toast, popup, put_buttons
from pywebio import start_server, config
from utils.get_config import config_data
import base64


def ai_agent_api(question: str, path: str = "/ask-agent/", url="http://127.0.0.1:" + str(config_data["server_port"])):
    # Use httpx to send a request to the /ask-agent/ endpoint of another server
    with httpx.Client(timeout=180.0) as client:
        try:
            response = client.post(url + path, json={"question": question})
            # Check response status code
            if response.status_code == 200:
                print(response.json()["ans"])
                return response.json()["ans"]
            else:
                return None
        except httpx.RequestError as e:
            print(e)
            # Handle request error
            return None


def upload_csv_api(file_content, table_name="uploaded_data"):
    url = f"http://127.0.0.1:{config_data['server_port']}/upload-csv/"
    files = {
        'file': ('data.csv', file_content, 'text/csv')
    }
    data = {
        'table_name': table_name
    }
    with httpx.Client(timeout=30.0) as client:
        try:
            response = client.post(url, files=files, data=data)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"{response.status_code}", "details": response.text}
        except httpx.RequestError as e:
            return {"error": f"{str(e)}"}


def upload_doc_api(file_content, filename, table_name="uploaded_data"):
    url = f"http://127.0.0.1:{config_data['server_port']}/upload-txt/"
    files = {
        'file': (filename, file_content, 'application/octet-stream')
    }
    data = {
        'table_name': table_name
    }
    with httpx.Client(timeout=30.0) as client:
        try:
            response = client.post(url, files=files, data=data)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"{response.status_code}", "details": response.text}
        except httpx.RequestError as e:
            return {"error": f"{str(e)}"}


def handle_csv_upload():
    file_info = file_upload(
        "Please select a CSV file to upload",
        accept=".csv",
        help_text="Select the CSV file you want to upload"
    )

    if file_info:
        table_name = input("Enter table name (optional, default is 'uploaded_data')", type=TEXT,
                           placeholder="uploaded_data", required=False)
        if not table_name:
            table_name = "uploaded_data"
        with put_loading(shape="grow", color="primary"):
            result = upload_csv_api(file_info['content'], table_name)
            print(result)
        err = result.get('type', "error")
        if err == "error":
            toast(f"Upload failed: {result}", color='error')
        else:
            toast("File uploaded successfully!", color='success')
            put_markdown("### Upload Results")
            put_markdown(f"Table name: `{result.get('table_name', table_name)}`")
            put_markdown(f"Row count: {result.get('row_count', 'N/A')}")
            put_markdown(f"Message: {result.get('message', 'N/A')}")


def handle_doc_upload():
    file_info = file_upload(
        "Please select a document file to upload (txt, doc, docx, pdf)",
        accept=".txt,.doc,.docx,.pdf",
        help_text="Select the document file you want to upload"
    )

    if file_info:
        table_name = input("Enter table name (optional, default is 'uploaded_data')", type=TEXT,
                           placeholder="uploaded_data", required=False)
        if not table_name:
            table_name = "uploaded_data"
        with put_loading(shape="grow", color="primary"):
            result = upload_doc_api(file_info['content'], file_info['filename'], table_name)
            print(result)

        if result.get('error'):
            toast(f"Upload failed: {result.get('error')}", color='error')
        else:
            toast("File uploaded successfully!", color='success')
            put_markdown("### Upload Results")
            put_markdown(f"Table name: `{result.get('table_name', table_name)}`")
            put_markdown(f"Extracted text length: {result.get('extracted_text_length', 'N/A')}")
            put_markdown(f"Preview: {result.get('preview', 'N/A')}")


@config(theme="dark")
def main():
    set_env(output_max_width='90%')

    # Load HTML content
    with open("DatasetExplorer.html", 'r', encoding='utf-8') as file:
        html_content = file.read()
    put_html(html_content)
    put_buttons(['Upload CSV File', 'Upload Document File'],
                onclick=[handle_csv_upload, handle_doc_upload])
    conversation_history = []

    while True:
        question = textarea("Enter your question here:", type=TEXT, rows=2)

        put_markdown("## " + question)

        if conversation_history:
            context = "\n".join(conversation_history[-6:])
            full_question = f"Context:\n{context}\n\nCurrent Question:\n{question}"
        else:
            full_question = question

        with put_loading():
            response = ai_agent_api(full_question, "/api/ask-agent/")
        if response:
            conversation_history.append(f"Q: {question}")
            conversation_history.append(f"A: {response}")

            put_markdown(response, sanitize=False)

        else:
            put_text("Failed to get a response from the AI Agent.")


# Start PyWebIO application
if __name__ == '__main__':
    start_server(main, port=8011)
