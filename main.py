import mimetypes

import pandas as pd
import sqlalchemy
import uvicorn
import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse, HTMLResponse, Response
from fastapi import File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.responses import JSONResponse

from agent.cot_chat import get_cot_chat
from data_access.insert_data_from_csv import process_csv_to_database
from utils.get_config import config_data

from agent.agent import exe_cot_code, get_cot_code, cot_agent
from agent.summary import get_ans_summary
from agent.ans_review import get_ans_review

# DATABASE_URL = config_data['mysql']
# engine = sqlalchemy.create_engine(DATABASE_URL)

app = FastAPI()

STATIC_FOLDER = "tmp_imgs"
STATIC_PATH = f"/{STATIC_FOLDER}"
# http://127.0.0.1:8003/tmp_imgs/mlkjcvep.png
@app.get(f"/{STATIC_FOLDER}/{{filename}}")
async def read_static_file(request: Request, filename: str):
    filepath = os.path.join(STATIC_FOLDER, filename)
    if os.path.isfile(filepath):
        # 猜测文件的MIME类型
        content_type, _ = mimetypes.guess_type(filepath)
        if content_type is None:
            content_type = "application/octet-stream"  # 默认为二进制流，如果无法确定类型
        # 读取文件内容
        with open(filepath, "rb") as file:
            file_content = file.read()
        # 返回Response对象，文件内容作为字节流发送
        return Response(content=file_content, media_type=content_type)
    else:
        return {"error": "File not found"}


class AgentInput(BaseModel):
    question: str


class AgentInputDict(BaseModel):
    question: str
    data: dict

class ReviewInput(BaseModel):
    question: str
    ans: str
    code: str


@app.post("/api/ask-agent/")
async def ask_agent(request: Request, user_input: AgentInput):
    ans, code = cot_agent(user_input.question)
    print(ans)
    if ans:
        processed_data = {
            "question": user_input.question,
            "ans": ans,
            "map": "",
            "type": "success",
            "msg": "处理成功"
        }
    else:
        processed_data = {
            "question": user_input.question,
            "ans": "",
            "map": "",
            "type": "error",
            "msg": "处理失败，请换个问法吧"
        }
    return JSONResponse(content=processed_data)


@app.post("/api/exe-code/")
async def exe_code(request: Request, user_input: AgentInput):
    ans = exe_cot_code(user_input.question)
    print(ans)
    if ans:
        processed_data = {
            "question": user_input.question,
            "ans": ans,
            "type": "success",
            "msg": "处理成功"
        }
    else:
        processed_data = {
            "question": user_input.question,
            "ans": "",
            "type": "error",
            "msg": "处理失败，请换个问法吧"
        }
    return JSONResponse(content=processed_data)


@app.post("/api/get-code/")
async def get_code(request: Request, user_input: AgentInput):
    code = get_cot_code(user_input.question)
    print(code)
    if code:
        processed_data = {
            "question": user_input.question,
            "code": code,
            "type": "success",
            "msg": "处理成功"
        }
    else:
        processed_data = {
            "question": user_input.question,
            "code": "",
            "type": "error",
            "msg": "处理失败，请换个问法吧"
        }
    return JSONResponse(content=processed_data)


@app.post("/api/review/")
async def get_code(request: Request, user_input: ReviewInput):
    ans = get_ans_review(user_input.question, user_input.ans, user_input.code)
    print(ans)
    if ans:
        processed_data = {
            "question": user_input.question,
            "ans": ans,
            "type": "success",
            "msg": "处理成功"
        }
    else:
        processed_data = {
            "question": user_input.question,
            "ans": "",
            "type": "error",
            "msg": "处理失败，请换个问法吧"
        }
    return JSONResponse(content=processed_data)


@app.post("/api/agent-summary/")
async def agent_summary(request: Request, user_input: AgentInput):
    ans = get_ans_summary(user_input.question)
    print(ans)
    if ans:
        processed_data = {
            "question": user_input.question,
            "ans": ans,
            "type": "success",
            "msg": "处理成功"
        }
    else:
        processed_data = {
            "question": user_input.question,
            "ans": "",
            "type": "error",
            "msg": "处理失败，请换个问法吧"
        }
    return JSONResponse(content=processed_data)


@app.post("/api/cot-chat/")
async def cot_chat(request: Request, user_input: AgentInput):
    ans = get_cot_chat(user_input.question)
    print(ans)
    if ans:
        processed_data = {
            "question": user_input.question,
            "ans": ans,
            "type": "success",
            "msg": "处理成功"
        }
    else:
        processed_data = {
            "question": user_input.question,
            "ans": "",
            "type": "error",
            "msg": "处理失败，请换个问法吧"
        }
    return JSONResponse(content=processed_data)


from agent.tools.copilot.utils.read_db import get_rows_from_all_tables
from agent.tools.tools_def import engine, llm
@app.post("/api/db-slice/")
async def db_slice(request: Request):
    first_five_rows = get_rows_from_all_tables(engine, None, num=5)
    from datetime import date, datetime
    def convert_date(obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return obj

    first_five_rows_json = {
        table_name: {
            "columns": rows.columns.tolist(),
            "data": [[convert_date(item) for item in row] for row in rows.values.tolist()]
        }
        for table_name, rows in first_five_rows.items()
    }

    processed_data = {
        "ans": first_five_rows_json,
        "type": "success",
        "msg": "处理成功"
    }

    return JSONResponse(content=processed_data)


@app.post("/api/get-sql/")
async def get_sql(request: Request):
    ans = ""
    processed_data = {
        "ans": ans,
        "type": "success",
        "msg": "处理成功"
    }

    return JSONResponse(content=processed_data)


@app.post("/api/exe-sql/")
async def exe_sql(request: Request, user_input: AgentInput):
    AgentInput.question
    ans = {}
    processed_data = {
        "ans": ans,
        "type": "success",
        "msg": "处理成功"
    }

    return JSONResponse(content=processed_data)


@app.post("/api/get-graph/")
async def get_graph_api(request: Request, user_input: AgentInputDict):
    df = pd.DataFrame.from_dict(user_input.data)
    user_input.question, df
    ans = ""
    if ans:
        processed_data = {
            "question": user_input.question,
            "ans": ans,
            "type": "success",
            "msg": "处理成功"
        }
    else:
        processed_data = {
            "question": user_input.question,
            "ans": "",
            "type": "error",
            "msg": "处理失败，请换个问法吧"
        }
    return JSONResponse(content=processed_data)


@app.post("/upload-csv/")
async def upload_csv(
        file: UploadFile = File(..., description="CSV file"),
        table_name: str = Form("uploaded_data")
):
    if not file.filename.lower().endswith('.csv'):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are supported"
        )
    try:
        content = await file.read()
        if len(content) == 0:
            raise HTTPException(status_code=400, detail="Uploaded file is empty")
        result = process_csv_to_database(content, table_name)
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File processing error: {str(e)}")



if __name__ == "__main__":
    uvicorn.run(app, host=config_data['server_host'], port=config_data['server_port'])
