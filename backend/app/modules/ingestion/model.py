from datetime import datetime

from sqlalchemy import DateTime, Index, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Log(Base):
	__tablename__ = "logs"
	__table_args__ = (
		Index("ix_logs_timestamp", "timestamp"),
		Index("ix_logs_service", "service"),
		Index("ix_logs_trace_id", "trace_id"),
	)

	id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
	timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
	service: Mapped[str] = mapped_column(String(120), nullable=False)
	level: Mapped[str] = mapped_column(String(20), nullable=False)
	message: Mapped[str] = mapped_column(Text, nullable=False)
	trace_id: Mapped[str | None] = mapped_column(String(120), nullable=True)
