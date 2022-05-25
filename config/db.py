from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import cloudinary

CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL").replace("cloudinary://", "")

api_key, CLOUDINARY_URL = CLOUDINARY_URL.split(':')
api_secret, cloud_name = CLOUDINARY_URL.split('@')

cloudinary.config(
    cloud_name = cloud_name,
    api_key = api_key,
    api_secret = api_secret
)


SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL").replace("postgres", "postgresql")
print(SQLALCHEMY_DATABASE_URL)


engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()