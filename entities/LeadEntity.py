from sqlalchemy import Column, String, Integer, DateTime
from configs.database import Base
# from pydantic import BaseModel


class customerModel(Base):
    __tablename__ = "customer_store"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), index=True)
    gender = Column(String(3))
    phone_number = Column(String(15))
    image = Column(String(100))
    email = Column(String(30))
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))