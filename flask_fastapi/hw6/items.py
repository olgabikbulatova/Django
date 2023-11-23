from typing import List

from fastapi import APIRouter, HTTPException
from db import items, database
from models import Item


router = APIRouter()


@router.get('/items/', response_model=List[Item])
async def get_items():
    query = items.select()
    return await database.fetch_all(query)


@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    query = items.select().where(items.c.id == item_id)
    return await database.fetch_one(query)


@router.post("/items/", response_model=Item)
async def create_item(item: Item):
    query = items.insert().values(item_name=item.item_name, description=item.description)
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, new_item: Item):
    query = items.update().where(items.c.id == item_id).values(**new_item.dict())
    await database.execute(query)
    return {**new_item.dict(), "id": item_id}


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await database.execute(query)
    return {'message': 'Item deleted'}