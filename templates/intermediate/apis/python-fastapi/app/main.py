from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="StickmansV4ult FastAPI Template", version="1.0.0")

class Item(BaseModel):
    name: str
    description: str | None = None

items: list[Item] = []

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def list_items():
    return items

@app.post("/items", status_code=201)
def create_item(item: Item):
    if not item.name.strip():
        raise HTTPException(status_code=400, detail="name is required")
    items.append(item)
    return item
