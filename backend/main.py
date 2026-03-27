from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "secret123"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

fake_user = {
    "username": "admin",
    "password": "1234"
}

tasks = []
task_id_counter = 1

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if (
        form_data.username != fake_user["username"] or
        form_data.password != fake_user["password"]
    ):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/tasks")
def get_tasks(status: str = None):
    if status:
        return [t for t in tasks if t["status"] == status]
    return tasks

@app.post("/tasks")
def create_task(task: dict):
    global task_id_counter
    task["id"] = task_id_counter
    task_id_counter += 1
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: dict, dep=Depends(verify_token)):
    for t in tasks:
        if t["id"] == task_id:
            t.update(updated)
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, dep=Depends(verify_token)):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {"message": "Deleted"}

@app.get("/tasks-summary")
def summary():
    pending = sum(1 for t in tasks if t["status"] == "pending")
    completed = sum(1 for t in tasks if t["status"] == "completed")
    return {"pending": pending, "completed": completed}