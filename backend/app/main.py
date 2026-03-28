from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import Base, engine
from app.modules.ingestion import model as ingestion_model
from app.modules.ingestion.api import router as ingestion_router


@asynccontextmanager
async def lifespan(_: FastAPI):
	# Ensure models are imported before metadata creation.
	_ = ingestion_model
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)
	yield


app = FastAPI(title="RootLens API", lifespan=lifespan)
app.include_router(ingestion_router)


@app.get("/health")
async def health() -> dict[str, str]:
	return {"status": "ok"}
