from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class CreateItemResponse(BaseModel):
    status: str
    item_id: int


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item) -> CreateItemResponse:
    return CreateItemResponse(status="OK", item_id=15)
