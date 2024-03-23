from fastapi import APIRouter, status
from typing import List
from mangum import Mangum
# Project Imports
from src.entities.schemas.api_schema import Item
from src.main import main_router, app
from fastapi.middleware.cors import CORSMiddleware

items = [{"name": "santi", "id": 1, "email": "santii@gmail.com"}]

router = APIRouter(prefix="/users")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@router.get("/items", response_model=List[Item])
async def read_item():
    return items

@router.post("/items", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    del items[item_id]
    return {"message" : "Item deleted"}

@router.get("/math/{num}")
async def math_operation(num: int):
    return num*num

main_router.include_router(router)
app.include_router(main_router)

handler = Mangum(app=app)