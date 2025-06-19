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
    <html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>シンプルサイト</title>
  <style>
    body { font-family: sans-serif; margin: 0; background: #f4f4f4; }
    header { background: #3498db; color: white; padding: 1em; text-align: center; }
    nav { background: #eee; padding: 0.5em; text-align: center; }
    nav a { margin: 0 10px; color: #333; text-decoration: none; }
    main { padding: 1em; max-width: 800px; margin: auto; background: white; }
    section { margin-bottom: 1.5em; }
    footer { text-align: center; padding: 1em; font-size: 0.9em; background: #ddd; }
  </style>
</head>
<body>

  <header>
    <h1>サンプルサイト</h1>
    <p>シンプルなWebページテンプレート</p>
  </header>

  <nav>
    <a href="#">ホーム</a>
    <a href="#">サービス</a>
    <a href="#">会社情報</a>
    <a href="#">連絡先</a>
  </nav>

  <main>
    <section>
      <h2>ようこそ！</h2>
      <p>これはHTMLとCSSだけで作られた簡単なテンプレートです。</p>
    </section>
    <section>
      <h2>特徴</h2>
      <ul>
        <li>シンプル構成</li>
        <li>すぐに使える</li>
        <li>カスタマイズ自由</li>
      </ul>
    </section>
  </main>

  <footer>
    &copy; 2025 シンプルサイト
  </footer>

</body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)