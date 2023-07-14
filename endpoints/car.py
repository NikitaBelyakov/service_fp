from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import CarIn, CarOut
from database import get_session, Car, Client
from models.car import CarsOut

router = APIRouter(prefix="/car", tags=["car"])


@router.get("/get", response_model=CarOut)
async def get_one(car_id: int,
                  session: Session = Depends(get_session)):
    car: Car = session.query(Car).get(car_id)
    if car:
        car_dto = CarOut(**car.__dict__)
        return car_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Car with id {car_id} not found!")


@router.get("/get_all", response_model=CarsOut)
async def get_all():
    session = get_session()
    cars = session.query(Car).all()
    cars_dto = list(map(lambda car: CarOut(**car.__dict__), cars))
    return CarsOut(cars=cars_dto)


@router.post("/create_car", response_model=CarOut)
async def create_car(car: CarIn):
    session = get_session()
    orm_car = Car(**car.dict())
    session.add(orm_car)
    print(orm_car.__dict__)
    session.commit()
    print(orm_car.__dict__)
    car_dto = CarOut(**orm_car.__dict__)
    return car_dto


@router.delete("/delete_car/{car_id}", response_model=CarOut)
async def delete_car(car_id: int, session: Session = Depends(get_session)):
    car: Car = session.query(Car).get(car_id)
    if car:
        car_dto = CarOut(**car.__dict__)
        session.delete(car)
        session.commit()
        return car_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"car with id {car_id} not found!")


@router.post("/update_car", response_model=CarOut)
async def update_car(car: CarIn):
    session = get_session()
    orm_car = session.query(Car).get(car.car_id)
    orm_car.brand = car.brand
    orm_car.color = car.color
    orm_car.vin_number = car.vin_number
    orm_car.main_owner_id = car.main_owner_id
    session.commit()
    car_dto = CarOut.from_orm(orm_car)
    return car_dto
