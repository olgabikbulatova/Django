from datetime import date, datetime
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
    user_id: int
    item_id: int
    create_date: datetime = Field(default=datetime.now())
    status: str = Field(default="created")


class Order(BaseModel):
    id: int
    user_id: int
    item_id: int
    create_date: datetime = Field(default=datetime.now())
    status: str = Field(default="created")