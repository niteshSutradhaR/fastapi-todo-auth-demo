from fastapi import FastAPI, HTTPException, Depends, Header
from app.schemas import Task, TaskCreate, UserLogin
from app.models import tasks_db, fake_user
from app.auth import create_access_token, verify_token

app = FastAPI()

def get_current_user(authorization: str = Header(None)):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization")
    token = authorization.split(" ")[1]
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload

@app.post("/login")
def login(user: UserLogin):
    if user.username == fake_user["username"] and user.password == fake_user["password"]:
        token = create_access_token({"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, user: dict = Depends(get_current_user)):
    new_task = Task(id=len(tasks_db)+1, **task.dict())
    tasks_db.append(new_task)
    return new_task

@app.get("/tasks/", response_model=list[Task])
def get_tasks(user: dict = Depends(get_current_user)):
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, user: dict = Depends(get_current_user)):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskCreate, user: dict = Depends(get_current_user)):
    for idx, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[idx] = Task(id=task_id, **updated_task.dict())
            return tasks_db[idx]
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, user: dict = Depends(get_current_user)):
    for idx, task in enumerate(tasks_db):
        if task.id == task_id:
            del tasks_db[idx]
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
