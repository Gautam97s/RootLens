from datetime import datetime

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.modules.ingestion.schema import LogLevel, LogRead
from app.modules.logs.schema import LogsListResponse
from app.modules.logs.service import get_logs

router = APIRouter(tags=["logs"])


@router.get("/logs", response_model=LogsListResponse)
async def list_logs(
	start_time: datetime | None = Query(default=None),
	end_time: datetime | None = Query(default=None),
	service: str | None = Query(default=None),
	level: LogLevel | None = Query(default=None),
	limit: int = Query(default=100, ge=1, le=1000),
	offset: int = Query(default=0, ge=0),
	db: AsyncSession = Depends(get_db),
) -> LogsListResponse:
	logs, total = await get_logs(
		db=db,
		start_time=start_time,
		end_time=end_time,
		service=service,
		level=level,
		limit=limit,
		offset=offset,
	)

	return LogsListResponse(
		total=total,
		limit=limit,
		offset=offset,
		items=[LogRead.model_validate(log) for log in logs],
	)
