from typing import Any

from varname import nameof

from Exceptions import CustomExistException
from models import models
from schemas import schemas
from config.db import Session
from services import generalServices
from services.generalServices import check_in_use_expression

_model = models.Genre

def create_genre(db: Session, model: schemas.GenreCreate) -> int:
    expression = _model.name == model.name
    check_in_use_expression(db=db, model=_model, expression=expression)
    genre = _model(name = model.name)
    db.add(genre)
    db.commit()
    return genre.id


def update_genre(db: Session, model: schemas.GenreCreate, expression: bool):
    genre = generalServices.get_by_expression(db=db, model=_model, expression=expression)
    if not model.name == genre.name:
        check_in_use_expression(db=db, model=_model, expression=_model.name == model.name)
        genre.name = model.name
        db.commit()
