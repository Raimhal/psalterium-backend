from datetime import datetime
from sqlalchemy import and_
from config.db import Session
from schemas import schemas
from services import generalServices
from models import models
_model = models.OrderBook



def add_to_basket(db: Session, model: schemas.OrderBookCreate, current_user: models.User) -> int:
    generalServices.check_in_warehouse(db=db, model=models.Book,  id=model.book_id, count=model.count)
    book = generalServices.get_by_expression(db=db, model=models.Book, expression=models.Book.id == model.book_id)
    order_book = db.query(_model).filter(and_(_model.order_id == 0, _model.book_id == model.book_id)).first()
    book.count -= model.count
    if order_book:
        order_book.count += model.count
        db.commit()
        return order_book.id
    else:
        _book = _model(
            order_id=0,
            consumer=current_user,
            book_id=book.id,
            count=model.count
        )
        db.add(_book)
        db.commit()
        return _book.id


def delete_from_basket(db: Session, id: int):
    order_book = generalServices.get_by_expression(db=db, model=_model, expression=_model.id == id)
    book = generalServices.get_by_expression(db=db, model=models.Book, expression=models.Book.id == order_book.book_id)
    book.count += order_book.count
    db.delete(order_book)
    db.commit()
