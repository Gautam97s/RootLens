from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.modules.ingestion.schema import LogCreate, LogRead
from app.modules.ingestion.service import create_log, create_logs

router = APIRouter(tags=["ingestion"])


@router.post("/ingest-log", response_model=LogRead, status_code=status.HTTP_201_CREATED)
async def ingest_log(payload: LogCreate, db: AsyncSession = Depends(get_db)) -> LogRead:
	log = await create_log(db, payload)
	return LogRead.model_validate(log)


@router.post("/ingest-logs", response_model=list[LogRead], status_code=status.HTTP_201_CREATED)
async def ingest_logs(payload: list[LogCreate], db: AsyncSession = Depends(get_db)) -> list[LogRead]:
	logs = await create_logs(db, payload)
	return [LogRead.model_validate(log) for log in logs]
