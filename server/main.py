from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends  # type: ignore[reportMissingImports]

from server.auth import require_api_key
from server.enrollment import router as enrollment_router
from server.enrollment import initialize_database
from server.devices import router as devices_router
from server.action_registry import router as actions_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield


app = FastAPI(
    title="SentinelRAT",
    description=(
        "Authorized endpoint monitoring and "
        "administration demonstration API."
    ),
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def root():
    return {
        "name": "SentinelRAT",
        "status": "online",
        "purpose": "Authorized endpoint monitoring",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/admin/status", dependencies=[Depends(require_api_key)])
def admin_status():
    return {
        "status": "operational",
        "service": "sentinelrat",
    }


app.include_router(enrollment_router)
app.include_router(devices_router)
app.include_router(actions_router)