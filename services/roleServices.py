from varname import nameof

from Exceptions import CustomExistException
from models import models
from schemas import schemas
from config.db import Session
from services import generalServices

_model = models.Role

def get_role(db: Session, name: str) -> _model:
    return db.query(_model).filter_by(name = name).first()


def create_role(db: Session, model: schemas.RoleCreate) -> int:
    _ = get_role(db=db, name=model.name)
    if _:
        CustomExistException(entity=_model, key=nameof(model.name), value=model.name)

    role = _model(name=model.name)
    db.add(role)
    db.commit()
    return role.id


def update_role(db: Session, model: schemas.RoleCreate, expression: bool):
    _ = get_role(db=db, name=model.name)
    if _:
        CustomExistException(entity=_model, key=nameof(model.name), value=model.name)

    role = generalServices.get_by_expression(db=db, model=_model, expression=expression)
    role.name = model.name
    db.commit()



