from datetime import datetime

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.ingestion.model import Log
from app.modules.ingestion.schema import LogLevel


async def get_logs(
	db: AsyncSession,
	start_time: datetime | None,
	end_time: datetime | None,
	service: str | None,
	level: LogLevel | None,
	limit: int,
	offset: int,
) -> tuple[list[Log], int]:
	filters = []

	if start_time is not None:
		filters.append(Log.timestamp >= start_time)
	if end_time is not None:
		filters.append(Log.timestamp <= end_time)
	if service is not None:
		filters.append(Log.service == service)
	if level is not None:
		filters.append(Log.level == level)

	query = (
		select(Log)
		.where(*filters)
		.order_by(Log.timestamp.desc())
		.limit(limit)
		.offset(offset)
	)
	total_query = select(func.count()).select_from(Log).where(*filters)

	result = await db.execute(query)
	total_result = await db.execute(total_query)

	return list(result.scalars().all()), int(total_result.scalar_one())
