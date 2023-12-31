from fastapi import FastAPI
from models import Hero, Relationship, RelationshipType, Ability, AbilityType
from sqlalchemy import select
from enum import Enum
from routes import heroes

app = FastAPI()
app.include_router(heroes.router)

@app.get("/")
async def read_root():
    return {"msg": "Hello World"}