"""FastAPI application entry point"""

from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.config import settings
from src.logging_config import setup_logging, get_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup and shutdown events"""
    # Startup
    setup_logging()
    logger = get_logger(__name__)
    logger.info(f"Starting {settings.app_name} v{settings.app_version}")
    logger.info(f"Debug mode: {settings.debug}")
    yield
    # Shutdown
    logger.info(f"Shutting down {settings.app_name}")


app = FastAPI(
    title=settings.app_name,
    description="API for comparing different sorting algorithms with performance instrumentation",
    version=settings.app_version,
    debug=settings.debug,
    lifespan=lifespan
)

logger = get_logger(__name__)


@app.get("/")
async def root():
    """Root endpoint"""
    logger.debug("Root endpoint accessed")
    return {
        "message": settings.app_name,
        "version": settings.app_version,
        "debug": settings.debug
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    logger.debug("Health check endpoint accessed")
    return {
        "status": "healthy",
        "app_name": settings.app_name,
        "version": settings.app_version
    }

