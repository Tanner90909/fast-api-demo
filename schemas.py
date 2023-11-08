from typing import Optional

from pydantic import BaseModel

# create these pydantic models (schemas)
# Heroes, Ability, AbilityTypes, Relationship, RelationshipType

# Data Model
class HeroModel(BaseModel):
    id: int
    name: str | None
    about_me: str | None
    biography: str | None
    image_url: str | None

    def __init__(self, **data):
        super().__init__(**data)
        
    class Config:
        from_attributes = True