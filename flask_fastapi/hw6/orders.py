from typing import List
from fastapi import APIRouter, HTTPException
from db import orders, database
from models import Order, OrderIn, User, Item
router = APIRouter()


@router.get('/orders/', response_model=List[Order])
async def get_orders():
    query = orders.select()
    return await database.fetch_all(query)


# @router.get("/orders/{user_id}", response_model=List[Order])
# async def read_order(user_id: int):
#     query = orders.select().where(orders.c.user.user_id == user_id)
#     return await database.fetch_all(query)


@router.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.order.id == order_id)
    return await database.fetch_one(query)


@router.post("/orders/", response_model=Order)
async def add_order(user: OrderIn):
    query = orders.insert().values(date=orders.date, user_id=orders.user_id, item_id=orders.item_id)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.dict())
    await database.execute(query)
    return {**new_order.dict(), "id": order_id}


@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted '}
