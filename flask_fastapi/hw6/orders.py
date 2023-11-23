from typing import List
from fastapi import APIRouter, HTTPException
from db import orders, database
from models import Order, OrderIn


router = APIRouter()


@router.get('/orders/', response_model=List[Order])
async def get_orders():
    query = orders.select()
    return await database.fetch_all(query)


@router.get("/orders/{user_id}", response_model=List[Order])
async def read_order(user_id: int):
    query = orders.select().where(orders.c.user_id == user_id)
    return await database.fetch_all(query)


@router.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    if not query:
        HTTPException(status_code=404, detail="order not found")
    return await database.fetch_one(query)


@router.post("/orders/", response_model=Order)
async def add_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id, item_id=order.item_id, create_date=order.date, status=order.status)
    last_record_id = await database.execute(query)
    return {**order.dict(), "id": last_record_id}


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
