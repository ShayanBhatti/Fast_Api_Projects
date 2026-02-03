from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import uuid4


class Task(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    estimated_time: Optional[int] = None   # in minutes
    completed: bool = False
    created_at: datetime


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    estimated_time: Optional[int] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    estimated_time: Optional[int] = None
    completed: Optional[bool] = None
