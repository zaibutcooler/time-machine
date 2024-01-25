from fastapi import FastAPI
from app.api import user #, auth

# Create FastAPI instance
app = FastAPI()

# Include routers for different API endpoints
app.include_router(user.router)
# app.include_router(auth.router)
