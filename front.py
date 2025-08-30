import httpx
from pywebio.session import set_env

from utils.get_config import config_data

from pywebio.input import input, TEXT, textarea
from pywebio.output import put_text, put_html, put_markdown, clear, put_loading
from pywebio import start_server, config

def ai_agent_api(question: str, path: str = "/ask-agent/", url="http://127.0.0.1:" + str(config_data["server_port"])):
    # 使用 httpx 发送请求到另一个服务器的 /ask-agent/ 接口
    with httpx.Client(timeout=180.0) as client:
        try:
            response = client.post(url+path, json={"question": question})
            # 检查响应状态码
            if response.status_code == 200:
                print(response.json()["ans"])
                return response.json()["ans"]
            else:
                return None
        except httpx.RequestError as e:
            print(e)
            # 处理请求错误
            return None

@config(theme="dark")
def main():
    set_env(output_max_width='90%')
    with open("DatasetExplorer.html", 'r', encoding='utf-8') as file:
        html_content = file.read()
    put_html(html_content)
    # 初始化对话历史
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

        # 检查响应并显示结果
        if response:
            # 将当前问答对添加到历史中
            conversation_history.append(f"Q: {question}")
            conversation_history.append(f"A: {response}")

            put_markdown(response, sanitize=False)

        else:
            put_text("Failed to get a response from the AI Agent.")


# 启动 PyWebIO 应用
if __name__ == '__main__':
    start_server(main, port=8010)
