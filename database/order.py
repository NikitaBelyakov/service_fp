from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base_meta import Base


class Order(Base):
    __tablename__ = 'orrder'
    __table_args__ = {'extend_existing': True}

    order_id = Column(Integer, primary_key=True)
    order_date = Column(Text, nullable=False)
    breakdown_name = Column(Text, nullable=False)
    car_id = Column(Integer, ForeignKey('car.car_id'))

    def __str__(self):
        return f"Клиенте {self.client_id}: {self.full_name}"