from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class ClientCar(Base):
    __tablename__ = 'client_car'
    __table_args__ = {'extend_existing': True}

    client_id = Column(ForeignKey("client.client_id"), primary_key=True)
    car_id = Column(ForeignKey("car.car_id"), primary_key=True)

    clients = relationship("Client", back_populates="cars")
    cars = relationship("Car", back_populates="clients")

    def __str__(self):
        return f"Клиент - автомобиль {self.client_id}: {self.car_id}"