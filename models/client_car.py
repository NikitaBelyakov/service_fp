from typing import List

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import ClientCar

ClientCarOut = sqlalchemy_to_pydantic(ClientCar)


class ClientCarIn(sqlalchemy_to_pydantic(ClientCar)):
    class Config:
        orm_mode = True


class ClientCarsOut(BaseModel):
    client_cars: List[ClientCarOut]
