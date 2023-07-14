from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship
from .base_meta import Base


class Client(Base):
    __tablename__ = 'client'
    __table_args__ = {'extend_existing': True}

    client_id = Column(Integer, primary_key=True)
    full_name = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    cars = relationship("ClientCar", backref='client')

    def __str__(self):
        return f"Клиенте {self.client_id}: {self.full_name}"