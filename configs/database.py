from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

DATABASE_URL = "mysql+mysqlconnector://root:@localhost/store"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def connect_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()