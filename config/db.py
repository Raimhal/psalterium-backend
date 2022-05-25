from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://hzjgbqnrvqlytl:94be1c27e89fa2667350997d342b852d06fe0d9b50b6956076dd45878f628b04@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/daf1l6gek0a5qt"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()