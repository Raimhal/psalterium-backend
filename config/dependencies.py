from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from starlette import status

from models import models
from schemas.schemas import TokenData
from . import SECRET_KEY, ALGORITHM
from .db import Session, Base, engine
from fastapi.security import OAuth2PasswordBearer
from services import generalServices, securityServices

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")

def create_database():
    Base.metadata.create_all(bind=engine)
    db: Session = Session()
    roles = db.query(entity:=models.Role).all()
    if not roles:
        admin_role = entity(name='Admin')
        user_role = entity(name='User')
        db.add_all([admin_role, user_role])
        db.commit()

    if 'Admin' not in [user.role.name for user in db.query(models.User).all()]:
        admin = models.User(
            email='admin@bookstore.com',
            password=securityServices.get_password_hash('admin'),
            username='Admin',
            role_id=1
        )
        db.add(admin)
        db.commit()




def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception

    model = models.User
    expression = model.email == token_data.email
    user = generalServices.get_by_expression(db=db, model=model, expression=expression)

    if user is None:
        raise credentials_exception
    return user
