# +Необходимо создать API для управления списком пользователей.
# +Создайте класс User с полями id, name, email и password.
# +API должен содержать следующие конечные точки:
# + GET /users — возвращает список пользователей.
# + GET /users/{id} — возвращает пользователя с указанным идентификатором.
# + POST /users — добавляет нового пользователя.
# + PUT /users/{id} — обновляет пользователя с указанным идентификатором.
# + DELETE /users/{id} — удаляет пользователя с указанным идентификатором.
# + Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
# + Для этого использовать библиотеку Pydantic.
# Задание по желанию
# + Создайте HTML шаблон для отображения списка пользователей.
# + Шаблон должен содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# + добавления нового пользователя.
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    name: str
    email: Optional[str]
    password: str


class UserInput(BaseModel):
    name: str
    email: Optional[str]
    password: str


users = [
    User(id=1, name='Olga', email='q@q.ru', password='123654'),
    User(id=2, name='Natasha', email='q1@q.ru', password='123789'),
    User(id=3, name='Marina', email='q2@q.ru', password='123987'),
]


@app.get("/{name}", response_class=HTMLResponse)
async def read_users(request: Request, name: str):
    return templates.TemplateResponse("users.html", {"request":request, "name": name, "users": users})


# @app.get('/users/')
# async def get_users():
#     return users


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    if len(users) < user_id:
        raise HTTPException(status_code=404, detail='task not found')
    return users[user_id-1]


@app.post("/users/add", response_model=list[User])
async def create_user(user: UserInput):
    user = User(
        id=len(users) + 1,
        name=user.name,
        email=user.email,
        password=user.password
    )
    users.append(user)
    return users


@app.put("/users/{user_id}", response_model=User)
async def change_task(user_id: int, new_user: UserInput):
    for user in users:
        if user.id == user_id:
            user.name = new_user.name,
            user.email = new_user.email,
            user.password = new_user.password
            return user
    raise HTTPException(status_code=404, detail='user not found')


@app.delete("/users/{user_id}", response_model=list[User])
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            del users[user_id-1]
            return users
    raise HTTPException(status_code=404, detail='user not found')

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
