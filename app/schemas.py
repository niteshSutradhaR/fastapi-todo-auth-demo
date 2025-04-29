from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str = None

class Task(TaskCreate):
    id: int

class UserLogin(BaseModel):
    username: str
    password: str
