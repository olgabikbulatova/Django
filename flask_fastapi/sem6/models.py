from datetime import date

from pydantic import BaseModel, Field


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(..., min_length=2)
    b_day: date = Field(..., format="%Y-%m-%d")
    email: str = Field(max_length=128)
    address: str = Field(max_length=128)
    password: str = Field(min_length=6)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    surname: str = Field(..., min_length=2)
    b_day: date = Field(..., format="%Y-%m-%d")
    email: str = Field(max_length=128)
    address: str = Field(max_length=128)


