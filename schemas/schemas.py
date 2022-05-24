from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


# books

class BookBase(BaseModel):
    name: str
    author: str
    content: Optional[str] = None
    price: float
    count: int
    publication_date: datetime
    ISBN: str

class BookCreate(BookBase):
    pass


class BookDto(BookBase):
    id: int
    owner_id: int
    image: str
    update_date: datetime

    class Config:
        orm_mode = True


# order book
class OrderBookBase(BaseModel):
    count: int
    book_id: int


class OrderBookCreate(OrderBookBase):
    pass

class OrderBook(OrderBookBase):
    id: int
    order_id: int
    consumer_id: int

    class Config:
        orm_mode = True



# users
class UserBase(BaseModel):
    email: str
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserCreate(UserBase):
    password: Optional[str] = None


class UserDto(UserBase):
    id: int
    role_id: int = None

    class Config:
        orm_mode = True


class User(UserDto):
    books: List[BookDto] = []

    class Config:
        orm_mode = True


# roles
class RoleBase(BaseModel):
    name: str


class RoleCreate(RoleBase):
    pass

class RoleDto(RoleBase):
    id: int

    class Config:
        orm_mode = True

class Role(RoleDto):
    users: List[UserDto] = []

    class Config:
        orm_mode = True


# token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


# orders
class OrderBase(BaseModel):
    deliver_date: datetime
    country: str
    city: str
    address: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    user_id: int
    books: List[OrderBook] = []

    class Config:
        orm_mode = True




# genres
class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class GenreDto(GenreBase):
    id: int

    class Config:
        orm_mode = True


class Genre(GenreDto):
    books: List[BookDto] = []

    class Config:
        orm_mode = True


class Book(BookDto):
    orders: List[OrderBook] = []
    genres: List[GenreDto] = []

    class Config:
        orm_mode = True












