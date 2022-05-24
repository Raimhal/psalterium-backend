from datetime import datetime

from sqlalchemy import Float, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, backref

from config.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    username = Column(String, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)

    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship('Role', back_populates='users')
    books = relationship('Book', back_populates='owner')
    basket = relationship('OrderBook', back_populates='consumer')

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    users = relationship('User', back_populates='role')

books_genres_temporary_table = \
    Table('books_genres', Base.metadata,
          Column('book_id', ForeignKey('books.id'), primary_key=True),
          Column('genre_id', ForeignKey('genres.id'), primary_key=True)
          )

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    content = Column(String)
    price = Column(Float, nullable=False)
    publication_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow)
    count = Column(Integer)
    image = Column(String, default='default.png')
    ISBN = Column(String, unique=True,index=True, nullable=False)

    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='books')
    orders = relationship('OrderBook', back_populates='book')
    genres = relationship('Genre', secondary=books_genres_temporary_table, back_populates='books', lazy=True)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    deliver_date = Column(DateTime)
    country = Column(String)
    city = Column(String)
    address = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    books = relationship('OrderBook', back_populates='order')

class OrderBook(Base):
    __tablename__ = 'orders_books'
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer)

    consumer_id = Column(Integer, ForeignKey('users.id'))
    consumer = relationship('User', back_populates='basket')
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship('Order', back_populates='books')
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship('Book', back_populates='orders')


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    books = relationship('Book', secondary=books_genres_temporary_table, back_populates='genres', lazy=True)

