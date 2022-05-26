
from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from Exceptions import CustomAccessForbiddenException
from config.db import Session
from config.decorators import raise_403_if_not_admin
from models import models
from schemas import schemas
from services import generalServices, userServices
from config.dependencies import get_db, get_current_user
_admin_role_name = 'Admin'

router = APIRouter(prefix='/users',tags=['users'])
_model = models.User

@router.get('', response_model=List[schemas.UserDto])
@raise_403_if_not_admin
async def get_users(skip: int=0, limit: int=10, db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user)):
    return generalServices.get_all(db=db, model=_model, skip=skip, limit=limit)


@router.get('/{id:int}', response_model=schemas.User)
@raise_403_if_not_admin
async def get_user_by_id(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    expression = _model.id == id
    return generalServices.get_by_expression(db=db, model=_model, expression=expression)


@router.get('/email', response_model=schemas.User)
@raise_403_if_not_admin
async def get_user_by_email(email: str, db: Session = Depends(get_db),
                            current_user: models.User = Depends(get_current_user)):
    expression = _model.email == email
    return generalServices.get_by_expression(db=db, model=_model, expression=expression)

@router.get("/me", response_model=schemas.UserDto)
async def get_current_user(current_user: models.User = Depends(get_current_user)):
    return current_user

@router.post('', response_model=int)
async def create_user(userCreate: schemas.UserCreate, db: Session = Depends(get_db)):
    return userServices.create_user(db=db, model=userCreate)


@router.put('/{id:int}/update', status_code=status.HTTP_204_NO_CONTENT)
async def update_user_by_id(id: int, userUpdate: schemas.UserCreate, db: Session = Depends(get_db),
                            current_user: models.User = Depends(get_current_user)):
    expression = _model.id == id
    if current_user.role.name == _admin_role_name:
        return userServices.update_user(db=db, model=userUpdate, expression=expression, current_user=current_user)

    if not current_user.id == id: CustomAccessForbiddenException()
    else:
        userServices.update_user(db=db, model=userUpdate, expression=expression, current_user=current_user)


@router.put('/email/update', status_code=status.HTTP_204_NO_CONTENT)
async def update_user_by_email(email: str, userUpdate: schemas.UserCreate, db: Session = Depends(get_db),
                               current_user: models.User = Depends(get_current_user)):
    expression = _model.email == email
    if current_user.role.name == _admin_role_name:
        return userServices.update_user(
            db=db,
            model=userUpdate,
            expression=expression,
            current_user=current_user
        )

    if not current_user.email == email:
        CustomAccessForbiddenException()
    else:
        userServices.update_user(db=db, model=userUpdate, expression=expression, current_user=current_user)


@router.patch('/{id:int}/change_role', status_code=status.HTTP_204_NO_CONTENT)
async def change_role(id: int, role_name: str, db: Session = Depends(get_db),
                            current_user: models.User = Depends(get_current_user)):
    userServices.change_user_role(db=db, user_id=id, role_name=role_name, current_user=current_user)


@router.delete('/{id:int}/delete', status_code=status.HTTP_204_NO_CONTENT)
@raise_403_if_not_admin
async def delete_user_by_id(id: int, db: Session = Depends(get_db),
                            current_user: models.User = Depends(get_current_user)):
    userServices.delete_user(db=db, id=id, current_user=current_user)

