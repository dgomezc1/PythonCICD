from app.main import app
from typing import List
from app.entities.models.model import Item

items = [{"name": "santi", "id": 1, "email": "santii@gmail.com"}]

@app.get("/items", response_model=List[Item])
async def read_item():
    return items

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

@app.delete("/items/{item_ud}")
async def delete_item(item_id: int):
    del items[item_id]
    return {"message" : "Item deleted"}