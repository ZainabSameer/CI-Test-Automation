from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    price: float

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@router.post("/items")
def create_item(item: Item):
    return {"item": item}
