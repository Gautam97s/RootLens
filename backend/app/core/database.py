from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings


class Base(DeclarativeBase):
	pass


connect_args: dict[str, object] = {}
if settings.database_url.startswith("postgresql+asyncpg") and settings.use_ssl_for_database:
	connect_args["ssl"] = True

engine = create_async_engine(
	settings.database_url,
	pool_pre_ping=True,
	connect_args=connect_args,
)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
	async with AsyncSessionLocal() as session:
		yield session
