import datetime
from typing import List, Any
from sqlalchemy import and_
from fastapi import UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.sql import text

from models import models
from schemas import schemas
from config.db import Session
from datetime import datetime
from . import generalServices, fileService
from Exceptions import CustomAccessForbiddenException



_model = models.Book

def get_sorted_books(db: Session, skip: int, limit: int, query: str, reverse: bool, genre: str, filter_expression: bool = True):
    expression = _model.name

    if query == 'author':
        expression = _model.author
    elif query == 'price':
        expression = _model.price
    elif query == 'count':
        expression = _model.count
    elif query == 'date':
        expression = _model.publication_date
    elif query == 'name':
        expression = _model.name

    if reverse:
        expression = expression.desc()

    if genre == 'all':
        genre_expression = True
    else:
        genre_entity = generalServices.get_by_expression(db=db, model=models.Genre, expression=models.Genre.name == genre)
        print(genre_entity)
        genre_expression = _model.genres.contains(genre_entity)

    filter = and_(genre_expression, filter_expression)

    return db.query(_model).filter(filter).order_by(expression).offset(skip).limit(limit).all()



def create_book(db: Session, model: schemas.BookCreate, current_user: models.User) -> int:
    expression = _model.ISBN == model.ISBN
    generalServices.check_in_use_expression(db=db, model=_model, expression=expression)
    book = _model(
        name=model.name,
        author=model.author,
        content=model.content,
        price=model.price,
        owner=current_user,
        count=model.count,
        publication_date=model.publication_date,
        ISBN=model.ISBN
    )
    db.add(book)
    db.commit()
    return book.id


def update_book(db: Session, model: schemas.BookCreate, expression: Any):
    book = generalServices.get_by_expression(db=db, model=_model, expression=expression)

    book.name = model.name
    book.author = model.author
    book.content = model.content
    book.price = model.price
    book.count = model.count
    book.update_date = datetime.utcnow()
    print(book.__dict__)
    if not book.ISBN == model.ISBN:
        expression = _model.ISBN == model.ISBN
        generalServices.check_in_use_expression(db=db, model=_model, expression=expression)
        book.ISBN = model.ISBN
    db.commit()


def set_genres(db: Session, genres: List[schemas.GenreBase], expression: Any):
    book = generalServices.get_by_expression(db=db, model=_model, expression=expression)
    book.genres = [
        generalServices.get_by_expression(
            db=db,
            model=(model:=models.Genre),
            expression=model.name == genre.name
        )
        for genre in genres
    ]
    db.commit()


def get_image(db: Session, id: int) -> FileResponse:
    book = generalServices.get_by_expression(db=db, model=_model, expression=_model.id == id)
    print(book.image)
    return fileService.get_file(book.image)


def get_image_by_name(name: str) -> FileResponse:
    return fileService.get_file(name)


def change_image(db: Session, image: UploadFile, expression: Any) -> str:
    book = generalServices.get_by_expression(db=db, model=_model, expression=expression)
    print(book.image)
    fileService.delete_file(book.image)
    book.image = fileService.save_file(image, 300)
    db.commit()
    print(book.image)
    return book.image



def delete_book(db: Session, id: int, current_user: models.User):
    book = generalServices.get_by_expression(db=db, model=_model, expression= _model.id == id)
    if(book.owner_id != current_user.id):
        CustomAccessForbiddenException()
    expression = models.OrderBook.book_id == book.id
    orders = generalServices.get_all_without_limit(db=db, model=models.OrderBook, expression=expression)
    for order in orders:
        if(order.order_id == 0):
            db.delete(order)
        else:
            expression = models.Order.id == order.order_id
            _order = generalServices.get_by_expression(db=db, model=models.Order, expression=expression)
            print(_order.books)
            _order.books.remove(order)
            print(_order.books)
            db.delete(order)
            if not _order.books:
                db.delete(_order)
    db.delete(book)
    db.commit()

