from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from entities.CustomerEntity import customerModel
from sqlalchemy.orm import relationship
from configs.database import Base
from sqlalchemy.sql import func

class addressModel(Base):
    __tablename__ = "address_store"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customer_store.id'))
    address = Column(String(30))
    district = Column(String(20))
    city = Column(String(20))
    province = Column(String(20))
    postal_code = Column(String(10))
    created_at = Column(DateTime(timezone=True), default=func.current_timestamp())
    updated_at = Column(DateTime(timezone=True), default=func.current_timestamp())

    customer = relationship("customerModel", back_populates="addresses")