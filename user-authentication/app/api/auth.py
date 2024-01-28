from fastapi import APIRouter, HTTPException
from app.models.user import User
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from databases import Database
from typing import List

# Database configuration
DATABASE_URL = "postgresql://username:password@localhost/dbname"

# SQLAlchemy
metadata = MetaData()
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True),
    Column("password", String),
)

# FastAPI Router
router = APIRouter()

# Database connection
database = Database(DATABASE_URL)


@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@router.post("/login/")
async def create_user(user: User):
    query = users.select().where(users.c.username == user.username)
    user_data = await database.fetch_one(query)
    if user_data is None or user_data['password'] != user.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = 'dummy_token'  # Generate token
    return {'token': token}


@router.post("/register/", response_model=User)
async def register(user: User):
    query = users.select().where(users.c.username == user.username)
    existing_user = await database.fetch_one(query)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Insert the new user into the database
    query = users.insert().values(username=user.username, password=user.password)
    await database.execute(query)
    
    return user
