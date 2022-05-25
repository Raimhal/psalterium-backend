from datetime import datetime
from sqlalchemy import and_
from config.db import Session
from schemas import schemas
from services import generalServices
from models import models
_model = models.Order


def create_order(db: Session, model: schemas.OrderCreate, current_user: models.User) -> int:
    order = _model(
        deliver_date=model.deliver_date,
        country=model.country,
        city=model.city,
        address=model.address,
        user_id=current_user.id,
    )
    db.add(order)
    expression = and_(models.OrderBook.order_id == None, models.OrderBook.consumer == current_user)
    order_books = generalServices.get_all_without_limit(db=db, model=models.OrderBook, expression=expression)
    for order_book in order_books:
        order_book.order = order
    db.commit()
    return order.id


def delete_order(db: Session, id: int):
    order = generalServices.get_by_expression(db=db, model=_model, expression=_model.id == id)
    expression = models.OrderBook.order == order
    order_books = generalServices.get_all_without_limit(db=db, model=models.OrderBook, expression=expression)
    for order_book in order_books:
        book = generalServices.get_by_expression(db=db, model=models.Book, expression=models.Book.id == order_book.book_id)
        book.count += order_book.count
        db.delete(order_book)
        db.commit()
    generalServices.delete(db=db, model=_model, id=id)
    db.commit()

