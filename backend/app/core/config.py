import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
	database_url: str = os.getenv(
		"DATABASE_URL",
		"postgresql+asyncpg://postgres:postgres@localhost:5432/rootlens",
	)


settings = Settings()
