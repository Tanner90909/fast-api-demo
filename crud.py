from schemas import HeroModel
from sqlalchemy.orm import Session, aliased, joinedload
from models import Hero, Ability, AbilityType, Relationship, RelationshipType

def get_heroes_v1(db:Session):
    # set a variable to store the query info
    heroes_query = (
        db.query(Hero).all()
    )

    return heroes_query

def get_heroes(db:Session):
    # set a variable to store the query info
    heroes_query = (
        db.query(Hero)
        .join(Hero.abilities)
        .all()
    )

    return heroes_query