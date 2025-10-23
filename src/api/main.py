"""FastAPI application entry point"""

from fastapi import FastAPI

app = FastAPI(
    title="Sorting Algorithm Comparison API",
    description="API for comparing different sorting algorithms with performance instrumentation",
    version="0.1.0"
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Sorting Algorithm Comparison API",
        "version": "0.1.0"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

