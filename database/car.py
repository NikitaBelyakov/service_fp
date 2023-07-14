from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base_meta import Base


class Car(Base):
    __tablename__ = 'car'
    __table_args__ = {'extend_existing': True}

    car_id = Column(Integer, primary_key=True)
    brand = Column(Text, nullable=False)
    color = Column(Text, nullable=False)
    vin_number = Column(Text, nullable=False)
    main_owner_id = Column(Integer, ForeignKey('client.client_id'))
    clients = relationship("ClientCar", backref="car")

    def __str__(self):
        return f"Автомобиль {self.car_id}: {self.brand} {self.vin_number}"