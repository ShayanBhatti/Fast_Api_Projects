# routes.py
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from datetime import datetime
from uuid import uuid4
from storage import load_tasks, save_tasks
from model import Task

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# -----------------------------
# Home Page — List all tasks
# -----------------------------
@router.get("/")
def home(request: Request):
    tasks = load_tasks()
    # sort tasks: incomplete first
    tasks.sort(key=lambda x: x["completed"])
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})


# -----------------------------
# Add Task
# -----------------------------
@router.post("/add")
def add_task(
    title: str = Form(...),
    description: str = Form(None),
    estimated_time: int = Form(None)
):
    tasks = load_tasks()

    new_task = Task(
        id=str(uuid4()),
        title=title,
        description=description,
        estimated_time=estimated_time,
        completed=False,
        created_at=datetime.now()
    )

    tasks.append(new_task.dict())
    save_tasks(tasks)

    # redirect back to homepage
    return RedirectResponse("/", status_code=303)


# -----------------------------
# Update Task — For editing title, desc, time
# -----------------------------
@router.post("/update/{task_id}")
def update_task(
    task_id: str,
    title: str = Form(None),
    description: str = Form(None),
    estimated_time: int = Form(None),
    completed: str = Form(None)  # optional checkbox
):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if title:
                task["title"] = title
            if description is not None:
                task["description"] = description
            if estimated_time is not None:
                task["estimated_time"] = estimated_time
            if completed is not None:
                # form checkbox sends "on" when checked
                task["completed"] = True if completed == "on" else False

            save_tasks(tasks)
            return RedirectResponse("/", status_code=303)

    raise HTTPException(status_code=404, detail="Task not found")


# -----------------------------
# Complete Task — Mark as completed
# -----------------------------
@router.post("/complete/{task_id}")
def complete_task(task_id: str):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            return RedirectResponse("/", status_code=303)
    raise HTTPException(status_code=404, detail="Task not found")


# -----------------------------
# Delete Task
# -----------------------------
@router.post("/delete/{task_id}")
def delete_task(task_id: str):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    save_tasks(new_tasks)
    return RedirectResponse("/", status_code=303)
