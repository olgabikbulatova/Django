from datetime import date
from pydantic import BaseModel, Field


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(..., min_length=2)
    email: str = Field(max_length=128)
    password: str = Field(min_length=6)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    surname: str = Field(..., min_length=2)
    email: str = Field(max_length=128)
    password: str = Field(min_length=6)


class Item(BaseModel):
    id: int
    item_name: str = Field(max_length=128)
    description: str = Field(max_length=128)
    price: float


class OrderIn(BaseModel):
    date: date = Field(format="%Y-%m-%d")
    user_id: int
    item_id: int


class Order(BaseModel):
    id: int
    date: date = Field(format="%Y-%m-%d")
    user_id: int
    item_id: int
