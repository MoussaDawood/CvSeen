from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = "sqlite:///./short_urls.db"

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://mobrillio:bGDneRaqHiSQpOm0aOWk@shorturls.c3cso6uqm2i5.eu-north-1.rds.amazonaws.com:3306/shorturls"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

