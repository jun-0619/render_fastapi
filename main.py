from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse #インポート

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    
    return {"result" : omikuji_list[random.randrange(10)]}


@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。最近いきなり暑くなりすぎて、CPU温度が爆上がりです。PC掃除してください。"}  # f文字列というPythonの機能を使っている


@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>a little HTML in here</title>
        </head>
        <body>
            <h1>日記  6/19(金)</h1>
            <p>
            今日は誕生日でした。でも特に普段と変わらずという感じの一日でした。<br>
            また、今日は夏季インターンの面接もありました。初めてのインターン面接だったのでとても緊張しましたが、一応きちんとした受け答えはできたつもりです。<br>
            でも面接官の雰囲気的に確実に落ちた気がします。とてもつらい。
            </p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)