from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from Exceptions import CustomAccessForbiddenException
from config.db import Session
from config.decorators import raise_403_if_not_admin
from models import models
from schemas import schemas
from services import generalServices, genreServices
from config.dependencies import get_db, get_current_user

router = APIRouter(prefix='/genres', tags=['genres'])
_model = models.Genre


@router.get('', response_model=List[schemas.GenreDto])
async def get_genres(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    return generalServices.get_all(db=db, model=_model, skip=skip, limit=limit)

@router.get('/all', response_model=List[schemas.GenreDto])
async def get_genres(db: Session = Depends(get_db)):
    return generalServices.get_all_without_limit(db=db, model=_model, expression=True)

@router.get('/{id:int}', response_model=schemas.Genre)
async def get_genre_by_id(id: int, db: Session = Depends(get_db)):
    expression = _model.id == id
    return generalServices.get_by_expression(db=db, model=_model, expression=expression)


@router.get('/name', response_model=schemas.Genre)
async def get_genre_by_name(name: str, db: Session = Depends(get_db)):
    expression = _model.name == name
    return generalServices.get_by_expression(db=db, model=_model, expression=expression)


@router.post('', response_model=int)
@raise_403_if_not_admin
async def create_genre(genreCreate: schemas.GenreCreate, db: Session = Depends(get_db),
                      current_user: models.User = Depends(get_current_user)):
    return genreServices.create_genre(db=db, model=genreCreate)


@router.put('/{id:int}/update', status_code=status.HTTP_204_NO_CONTENT)
@raise_403_if_not_admin
async def update_genre(id: int, genreUpdate: schemas.GenreCreate, db: Session = Depends(get_db),
                            current_user: models.User = Depends(get_current_user)):
    expression = _model.id == id
    genreServices.update_genre(db=db, model=genreUpdate, expression=expression)


@router.delete('/{id}/delete', status_code=status.HTTP_204_NO_CONTENT)
@raise_403_if_not_admin
async def delete_genre(id: int, db: Session = Depends(get_db),
                            current_user: models.User = Depends(get_current_user)):
    generalServices.delete(db=db, model=_model, id=id)

