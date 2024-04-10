from fastapi import APIRouter, HTTPException
from models.user import User
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from databases import Database
from typing import List
from main import database_url

# # Database configuration

# SQLAlchemy
metadata = MetaData()
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True),
    Column("password", String),
)

router = APIRouter()

database = Database(database_url)


@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@router.post("/login/")
async def login(user: User):

    

    token = "token"
    return {'token': token}


@router.post("/register/", response_model=User)
async def register(user: User):
    
    query = users.insert().values()


    return user
