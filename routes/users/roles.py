from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from config.db import Session
from config.decorators import raise_403_if_not_admin
from models import models
from schemas import schemas
from services import generalServices, roleServices
from config.dependencies import get_db, get_current_user
from Exceptions import CustomAccessForbiddenException

router = APIRouter(prefix='/roles', tags=['roles'])
_admin_role_name = 'Admin'
_model = models.Role

@router.get('', response_model=List[schemas.RoleDto])
@raise_403_if_not_admin
async def get_roles(skip: int=0, limit: int=10, db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user)):
    return generalServices.get_all(db=db, model=models.Role, skip=skip, limit=limit)


@router.get('/{id:int}', response_model=schemas.Role)
@raise_403_if_not_admin
async def get_role_by_id(id: int, db: Session = Depends(get_db),
                         current_user: models.User = Depends(get_current_user)):
    expression = _model.id == id
    return generalServices.get_by_expression(db=db, model=_model, expression=expression)


@router.get('/name', response_model=schemas.Role)
@raise_403_if_not_admin
async def get_role_by_name(name: str, db: Session = Depends(get_db),
                           current_user: models.User = Depends(get_current_user)):
    expression = _model.name == name
    return generalServices.get_by_expression(db=db, model=_model, expression=expression)


@router.post('', response_model=int)
@raise_403_if_not_admin
async def create_role(roleCreate: schemas.RoleCreate, db: Session = Depends(get_db),
                      current_user: models.User = Depends(get_current_user)):
    return roleServices.create_role(db=db, model=roleCreate)


@router.put('/{id:int}/update', status_code=status.HTTP_204_NO_CONTENT)
@raise_403_if_not_admin
async def update_role_by_id(id: int, roleUpdate: schemas.RoleCreate, db: Session = Depends(get_db),
                            current_user: models.User = Depends(get_current_user)):
    expression = _model.id == id
    roleServices.update_role(db=db, model=roleUpdate, expression=expression)


@router.delete('/{id:int}/delete', status_code=status.HTTP_204_NO_CONTENT)
@raise_403_if_not_admin
async def delete_role_by_id(id: int, db: Session = Depends(get_db),
                            current_user: models.User = Depends(get_current_user)):
    generalServices.delete(db=db, model=models.Role, id=id)

