from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from configs.database import Base
from sqlalchemy.sql import func


class customerModel(Base):
    __tablename__ = "customer_store"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), index=True)
    name = Column(String(30))
    gender = Column(String(3))
    phone_number = Column(String(15))
    image = Column(String(100))
    email = Column(String(30))
    created_at = Column(DateTime(timezone=True), default=func.current_timestamp())
    updated_at = Column(DateTime(timezone=True),default=func.current_timestamp())

    addresses = relationship("addressModel", back_populates="customer")