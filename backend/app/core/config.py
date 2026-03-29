import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


def _load_environment_files() -> None:
	backend_root = Path(__file__).resolve().parents[2]
	workspace_root = backend_root.parent

	# Order matters: backend/.env can override shared infra defaults.
	env_files = [
		workspace_root / "infra" / "env" / "backend.env",
		backend_root / ".env",
	]

	for env_file in env_files:
		if env_file.exists():
			load_dotenv(env_file, override=True)


def _to_bool(value: str | None, default: bool = False) -> bool:
	if value is None:
		return default
	return value.strip().lower() in {"1", "true", "yes", "on"}


_load_environment_files()


@dataclass(frozen=True)
class Settings:
	database_url: str = os.getenv(
		"DATABASE_URL",
		"postgresql+asyncpg://postgres:postgres@localhost:5432/rootlens",
	)
	database_ssl: bool = _to_bool(os.getenv("DATABASE_SSL"), default=False)

	@property
	def use_ssl_for_database(self) -> bool:
		# Neon endpoints require SSL. You can also force this via DATABASE_SSL=true.
		return self.database_ssl or "neon.tech" in self.database_url


settings = Settings()
