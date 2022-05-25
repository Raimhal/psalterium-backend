from fastapi import APIRouter, Depends
from typing import List
from models import models
from schemas import schemas
from services import generalServices, basketService
from config.dependencies import get_db, get_current_user
from config.db import Session
from starlette import status
from Exceptions import CustomAccessForbiddenException
from sqlalchemy import and_

router = APIRouter(prefix='/basket', tags=['basket'])
_model = models.OrderBook
_admin_role_name = 'Admin'




@router.get('', response_model=List[schemas.OrderBook])
async def basket(skip: int=0, limit: int=10, db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user)):
    expression = and_(_model.order_id == None, _model.consumer == current_user)
    return generalServices.get_all_with_expression(db=db, model=_model, skip=skip, limit=limit, expression=expression)


@router.post('', response_model=int)
async def add_to_basket(orderBookCreate: schemas.OrderBookCreate, db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user)):
    return basketService.add_to_basket(db=db, model=orderBookCreate, current_user=current_user)

@router.delete('/{id:int}/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_from_basket(id: int, db: Session = Depends(get_db),
                    current_user: models.User = Depends(get_current_user)):
    return basketService.delete_from_basket(db=db, id=id)
