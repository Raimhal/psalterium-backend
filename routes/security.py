from datetime import timedelta

from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from config import ACCESS_TOKEN_EXPIRE_MINUTES
from config.db import Session
from config.dependencies import get_db
from schemas import schemas
from services.securityServices import authenticate_user, create_access_token

router = APIRouter(tags=['security'])

@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db=db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "role": user.role.name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}