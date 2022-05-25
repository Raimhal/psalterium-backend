from typing import List, Optional

from fastapi import APIRouter, Depends, UploadFile, File
from starlette import status
from sqlalchemy import or_
from config.db import Session
from models import models
from schemas import schemas
from services import generalServices, bookServices
from config.dependencies import get_db, get_current_user
from Exceptions import CustomAccessForbiddenException

router = APIRouter(prefix='/books', tags=['books'])
_admin_role_name = 'Admin'
_model = models.Book


@router.get('/unsorted', response_model=List[schemas.BookDto])
async def get_books(skip: int=0, limit: int=10, db: Session = Depends(get_db)):
    return generalServices.get_all(db=db, model=_model, skip=skip, limit=limit)


@router.get('', response_model=List[schemas.BookDto])
async def get_books(query: str = 'name', reverse: bool = False, skip: int=0, limit: int=10, genre: str = 'all',
                    db: Session = Depends(get_db)):
    return bookServices.get_sorted_books(db=db, skip=skip, limit=limit, query=query, reverse=reverse, genre=genre)


@router.get('/search', response_model=List[schemas.BookDto])
async def get_books(searchQuery: str, query: str = 'name', reverse: bool = False, skip: int=0, genre: str = 'all',
                    limit: int=10, db: Session = Depends(get_db)):
    expression = or_(_model.name.contains(searchQuery.lower()), _model.name.contains(searchQuery.lower().capitalize()))
    return bookServices.get_sorted_books(db=db, skip=skip, limit=limit, query=query, reverse=reverse, genre=genre, filter_expression=expression)


@router.get('/my', response_model=List[schemas.BookDto])
async def get_books(query: str = 'name', reverse: bool = False, skip: int=0, limit: int=10, genre: str = 'all',
                    db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    expression = _model.owner == current_user
    if current_user.role.name == _admin_role_name:
        expression = True
    return bookServices.get_sorted_books(db=db, skip=skip, limit=limit, query=query, reverse=reverse, genre=genre, filter_expression=expression)


@router.get('/{id:int}', response_model=schemas.Book)
async def get_book(id: int, db: Session = Depends(get_db)):
    expression = _model.id == id
    return generalServices.get_by_expression(db=db, model=_model, expression=expression)

@router.get('/{id:int}/dto', response_model=schemas.BookDto)
async def get_book_dto(id: int, db: Session = Depends(get_db)):
    expression = _model.id == id
    return generalServices.get_by_expression(db=db, model=_model, expression=expression)


@router.get("/{id:int}/image", status_code=status.HTTP_200_OK)
async def get_image(id: int, db: Session = Depends(get_db)):
    return bookServices.get_image(db=db, id=id)


@router.get("/image", status_code=status.HTTP_200_OK)
async def get_image(name: str):
    return bookServices.get_image_by_name(name)


@router.post('', response_model=int)
async def create_book(bookCreate: schemas.BookCreate,db: Session = Depends(get_db),
                      current_user: models.User = Depends(get_current_user)):
    return bookServices.create_book(db=db, model=bookCreate, current_user=current_user)


@router.put('/{id:int}/update', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(id: int, bookUpdate: schemas.BookCreate,
                      db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    expression = _model.id == id
    bookServices.update_book(db=db, model=bookUpdate, expression=expression)


@router.patch('/{id:int}/set_genres', status_code=status.HTTP_204_NO_CONTENT)
async def set_genres(id: int, genres: List[schemas.GenreBase], db: Session = Depends(get_db),
                            current_user: models.User = Depends(get_current_user)):
    expression = _model.id == id
    bookServices.set_genres(db=db, genres=genres, expression=expression)


@router.patch('/{id:int}/change_image', response_model=str)
async def change_image(id: int, db: Session = Depends(get_db), file: UploadFile = File(...),
                       current_user: models.User = Depends(get_current_user)):
    expression = _model.id == id
    return bookServices.change_image(db=db, image=file, expression=expression)


@router.delete('/{id}/delete', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int, db: Session = Depends(get_db),
                            current_user: models.User = Depends(get_current_user)):
    bookServices.delete_book(db=db, id=id)


