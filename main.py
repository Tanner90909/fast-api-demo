from fastapi import FastAPI
from models import Hero, Relationship, RelationshipType, Ability, AbilityType
import database
from sqlalchemy import select

app = FastAPI()

@app.get("/")
async def read_root():
    return "hello world"