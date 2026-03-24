import asyncio
import uuid
from fastapi import APIRouter, HTTPException

from app.models.schemas import CommandRequest, TaskStatus
from app.agents.team_lead import decompose_command
from app.agents.team_member import execute_task
from app.agents.reporter import create_report
from app.db import save_command, update_command, get_commands

router = APIRouter()


@router.post("/commands")
async def create_command(req: CommandRequest):
    command_id = str(uuid.uuid4())[:8]

    # 1. 팀장이 명령을 분해
    plan_data = await decompose_command(req.message)
    subtasks = plan_data["subtasks"]

    await save_command(
        command_id=command_id,
        message=req.message,
        plan=plan_data["plan"],
        subtasks=subtasks,
        status=TaskStatus.IN_PROGRESS,
    )

    # 2. 팀원들이 병렬로 작업 수행
    async def run_subtask(task: dict) -> dict:
        result = await execute_task(task["assignee"], task["description"])
        task["result"] = result
        task["status"] = TaskStatus.COMPLETED
        return task

    completed = await asyncio.gather(
        *[run_subtask(t) for t in subtasks],
        return_exceptions=True,
    )

    # 실패 처리
    results = []
    for i, r in enumerate(completed):
        if isinstance(r, Exception):
            subtasks[i]["status"] = TaskStatus.FAILED
            subtasks[i]["result"] = str(r)
        else:
            results.append(r)

    # 3. 보고서 작성
    final_report = await create_report(req.message, results)

    await update_command(
        command_id=command_id,
        subtasks=subtasks,
        final_report=final_report,
        status=TaskStatus.COMPLETED,
    )

    return {
        "command_id": command_id,
        "plan": plan_data["plan"],
        "subtasks": subtasks,
        "final_report": final_report,
        "status": "completed",
    }


@router.get("/commands")
async def list_commands():
    return await get_commands()


@router.get("/commands/{command_id}")
async def get_command(command_id: str):
    commands = await get_commands(limit=100)
    for cmd in commands:
        if cmd["id"] == command_id:
            return cmd
    raise HTTPException(status_code=404, detail="Command not found")
