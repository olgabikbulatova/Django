# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.


from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: bool


class TaskInput(BaseModel):
    title: str
    description: Optional[str]
    status: bool


tasks = [
    Task(id=1, title='abc', description='sadghasd', status=True)
]


@app.get('/tasks/')
async def get_tasks():
    return tasks


@app.post('/tasks', response_model=list[Task])
async def create_task(task: TaskInput):
    task = Task(
        id=len(tasks) + 1,
        title=task.title,
        description=task.description,
        status=task.status
    )
    tasks.append(task)
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    if len(tasks) < task_id:
        raise HTTPException(status_code=404, detail='task not found')
    return tasks[task_id-1]


@app.get("/tasks/{task_status}", response_model=list[TaskInput])
async def filter_task(task_status: bool):
    result = []
    for task in tasks:
        if task.status == task_status:
            result.append(task)
        raise HTTPException(status_code=404, detail='task not found')
    return result


@app.put("/tasks/edit", response_model=Task)
async def change_task(task_id: int, new_task: TaskInput):
    for task in tasks:
        if task.id == task_id:
            task.title = new_task.title,
            task.description = new_task.description,
            task.status = new_task.status
            return task
    raise HTTPException(status_code=404, detail='task not found')


@app.delete("/tasks/del")
async def delete_task(task_id: int):
    if len(tasks) < task_id:
        raise HTTPException(status_code=404, detail='task not found')
    tasks.pop(task_id)
    return tasks


if __name__ == '__main__':
    uvicorn.run("task1:app", host="127.0.0.1", port=8000, reload=True)