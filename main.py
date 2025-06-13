from typing import Optional

from fastapi import FastAPI
from omikuji import router as omikuji_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

app.include_router(omikuji_router)  # ここでルーターを登録