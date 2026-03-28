from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.ingestion.model import Log
from app.modules.ingestion.schema import LogCreate


async def create_log(db: AsyncSession, payload: LogCreate) -> Log:
	db_log = Log(**payload.model_dump())
	db.add(db_log)
	await db.commit()
	await db.refresh(db_log)
	return db_log


async def create_logs(db: AsyncSession, payloads: list[LogCreate]) -> list[Log]:
	db_logs = [Log(**payload.model_dump()) for payload in payloads]
	db.add_all(db_logs)
	await db.commit()
	for log in db_logs:
		await db.refresh(log)
	return db_logs
