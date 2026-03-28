from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class LogLevel(str, Enum):
	debug = "DEBUG"
	info = "INFO"
	warning = "WARNING"
	error = "ERROR"
	critical = "CRITICAL"


class LogCreate(BaseModel):
	timestamp: datetime
	service: str = Field(min_length=1, max_length=120)
	level: LogLevel
	message: str = Field(min_length=1)
	trace_id: str | None = Field(default=None, max_length=120)


class LogRead(LogCreate):
	model_config = ConfigDict(from_attributes=True)

	id: int
