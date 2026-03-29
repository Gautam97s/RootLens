from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.modules.ingestion import model as ingestion_model
from app.modules.ingestion.api import router as ingestion_router
from app.modules.logs.api import router as logs_router


@asynccontextmanager
async def lifespan(_: FastAPI):
	# Ensure models are imported before metadata creation.
	_ = ingestion_model
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)
	yield


app = FastAPI(title="RootLens API", lifespan=lifespan)
app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)
app.include_router(ingestion_router)
app.include_router(logs_router)


@app.get("/health")
async def health() -> dict[str, str]:
	return {"status": "ok"}
