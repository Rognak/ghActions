from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Config


SQLALCHEMY_DATABASE_URL = f"postgresql://{Config.PG_USER}:{Config.PG_PASS}@{Config.PG_HOST}:5432/{Config.PG_DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
