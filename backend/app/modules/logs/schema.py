from pydantic import BaseModel

from app.modules.ingestion.schema import LogRead


class LogsListResponse(BaseModel):
	total: int
	limit: int
	offset: int
	items: list[LogRead]
