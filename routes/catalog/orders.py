from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from Exceptions import CustomAccessForbiddenException
from config.db import Session
from config.decorators import raise_403_if_not_admin
from models import models
from schemas import schemas
from services import generalServices, genreServices, orderServices
from config.dependencies import get_db, get_current_user

router = APIRouter(prefix='/orders', tags=['orders'])
_model = models.Order
_admin_role_name = 'Admin'


@router.get('', response_model=List[schemas.Order])
@raise_403_if_not_admin
async def get_orders(skip: int=0, limit: int=10, db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user)):
    return generalServices.get_all(db=db, model=_model, skip=skip, limit=limit)


@router.get('/my', response_model=List[schemas.Order])
async def get_orders(skip: int=0, limit: int=10, db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user)):
    expression = _model.user_id == current_user.id
    return generalServices.get_all_with_expression(db=db, model=_model, skip=skip, limit=limit, expression=expression)


@router.get('/{id:int}', response_model=schemas.Order)
async def get_order(id: int, db: Session = Depends(get_db),
                         current_user: models.User = Depends(get_current_user)):
    expression = _model.id == id
    return generalServices.get_by_expression(db=db, model=_model, expression=expression)


@router.post('', response_model=int)
async def create_order(orderCreate: schemas.OrderCreate, db: Session = Depends(get_db),
                      current_user: models.User = Depends(get_current_user)):
    return orderServices.create_order(db=db, model=orderCreate, current_user=current_user)


@router.delete('/{id:int}/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(id: int, db: Session = Depends(get_db),
                            current_user: models.User = Depends(get_current_user)):
    orderServices.delete_order(db=db, id=id)

