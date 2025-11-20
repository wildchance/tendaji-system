from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from os import getenv

engine = create_engine(getenv("DATABASE_URL"))

SessionLocal = sessionmaker(bind=engine)
