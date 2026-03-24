import aiosqlite
import json
from datetime import datetime

DB_PATH = "aivc.db"


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS commands (
                id TEXT PRIMARY KEY,
                message TEXT NOT NULL,
                plan TEXT,
                subtasks TEXT,
                final_report TEXT,
                status TEXT DEFAULT 'pending',
                created_at TEXT NOT NULL
            )
        """)
        await db.commit()


async def save_command(command_id: str, message: str, plan: str, subtasks: list, status: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO commands (id, message, plan, subtasks, status, created_at) VALUES (?, ?, ?, ?, ?, ?)",
            (command_id, message, plan, json.dumps(subtasks, ensure_ascii=False), status, datetime.now().isoformat()),
        )
        await db.commit()


async def update_command(command_id: str, subtasks: list, final_report: str | None, status: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE commands SET subtasks = ?, final_report = ?, status = ? WHERE id = ?",
            (json.dumps(subtasks, ensure_ascii=False), final_report, status, command_id),
        )
        await db.commit()


async def get_commands(limit: int = 20) -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute(
            "SELECT * FROM commands ORDER BY created_at DESC LIMIT ?", (limit,)
        )
        rows = await cursor.fetchall()
        return [
            {
                "id": row["id"],
                "message": row["message"],
                "plan": row["plan"],
                "subtasks": json.loads(row["subtasks"]) if row["subtasks"] else [],
                "final_report": row["final_report"],
                "status": row["status"],
                "created_at": row["created_at"],
            }
            for row in rows
        ]
