from typing import List

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import Car

CarOut = sqlalchemy_to_pydantic(Car)


class CarIn(sqlalchemy_to_pydantic(Car)):
    class Config:
        orm_mode = True


class CarsOut(BaseModel):
    cars: List[CarOut]
