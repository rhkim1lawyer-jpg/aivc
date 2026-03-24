from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


class CommandRequest(BaseModel):
    message: str


class SubTask(BaseModel):
    id: int
    title: str
    assignee: str  # "researcher", "writer", "coder" 등
    description: str
    status: TaskStatus = TaskStatus.PENDING
    result: str | None = None


class CommandResponse(BaseModel):
    command_id: str
    original_message: str
    plan: str
    subtasks: list[SubTask]
    final_report: str | None = None
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime
