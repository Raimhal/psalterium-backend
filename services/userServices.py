from varname import nameof

from Exceptions import CustomExistException
from models import models
from schemas import schemas
from config.db import Session
from . import generalServices, securityServices, bookServices
from Exceptions import CustomAccessForbiddenException


_model = models.User
_role_model = models.Role

def check_email_in_use(db: Session, email: str) -> _model:
    return db.query(_model).filter(_model.email == email).first()

def create_user(db: Session, model: schemas.UserCreate) -> int:
    _ = check_email_in_use(db=db, email=model.email)
    if _:
        CustomExistException(entity=_model, key=nameof(model.email), value=model.email)

    user_role = generalServices.get_by_expression(db=db, model=_role_model, expression=_role_model.name == 'User')

    user = _model(
        email=model.email,
        username=model.username,
        first_name=model.first_name,
        last_name=model.last_name,
        password=securityServices.get_password_hash(model.password),
        role = user_role
    )

    db.add(user)
    db.commit()
    return user.id


def update_user(db: Session, model: schemas.UserCreate, expression: bool, current_user: models.User):

    user = generalServices.get_by_expression(db=db, model=_model, expression=expression)

    if(current_user.role.name != 'Admin' and user.id != current_user.id):
         CustomAccessForbiddenException()

    user.username = model.username
    user.first_name = model.first_name
    user.last_name = model.last_name
    if model.password:
        user.password = securityServices.get_password_hash(model.password)
    db.commit()

def change_user_role(db: Session, user_id: int, role_name: str, current_user: models.User):

    if(current_user.role.name != 'Admin' and user_id != current_user.id):
            CustomAccessForbiddenException()

    user = generalServices.get_by_expression(db=db, model=_model, expression=_model.id == user_id)
    role = generalServices.get_by_expression(
        db=db,
        model=_role_model,
        expression=_role_model.name == role_name.lower().capitalize()
    )
    user.role = role
    db.commit()

def delete_user(db: Session, id: int, current_user: models.User):
    user = generalServices.get_by_expression(db=db, model=_model, expression=_model.id == id)

    if(current_user.role.name != 'Admin' and id != current_user.id):
        CustomAccessForbiddenException()

    for book in user.books:
        bookServices.delete_book(db=db, id=book.id, current_user=current_user)
    generalServices.delete(db=db, model=_model, id=user.id)


