from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    # Initialize services or connections if needed
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Clean up resources if needed
    pass
