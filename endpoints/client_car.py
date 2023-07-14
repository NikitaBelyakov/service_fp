from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import ClientCarIn,ClientCarOut
from database import get_session, Client, Car, ClientCar
from models.client_car import ClientCarsOut

router = APIRouter(prefix="/client_car", tags=["client_car"])


@router.get("/get", response_model=ClientCarOut)
async def get_one(client_id: int, car_id: int,
                  session: Session = Depends(get_session)):
    client_car: ClientCar = session.query(ClientCar).get((client_id, car_id))
    if client_car:
        if client_car.client_id == client_id:
            client_car_dto = ClientCarOut(**client_car.__dict__)
            return client_car_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Client with id {client_id} not found!")


@router.get("/get_all", response_model=ClientCarsOut)
async def get_all():
    session = get_session()
    client_cars = session.query(ClientCar).all()
    client_cars_dto = list(map(lambda client_car: ClientCarOut(**client_car.__dict__), client_cars))
    return ClientCarsOut(client_cars=client_cars_dto)


@router.post("/create_client_car", response_model=ClientCarOut)
async def create_client_car(client_car: ClientCarIn):
    session = get_session()
    orm_client_car = ClientCar(**client_car.dict())
    session.add(orm_client_car)
    session.commit()
    client_car_dto = ClientCarOut(**orm_client_car.__dict__)
    return client_car_dto

@router.post("/update_client_car", response_model=ClientCarOut)
async def update_client_car(client_car: ClientCarIn):
    session = get_session()
    orm_client_car = session.query(ClientCar).get((client_car.client_id,client_car.car_id))
    session.commit()
    client_car_dto = ClientCarOut.from_orm(orm_client_car)
    return client_car_dto


@router.delete("/delete_client_car/{client_id}/{car_id}", response_model=ClientCarOut)
async def delete_client_car(client_id: int,car_id: int , session: Session = Depends(get_session)):
    client_car: ClientCar = session.query(ClientCar).get((client_id, car_id))
    if client_car:
        client_car_dto = ClientCarOut(**client_car.__dict__)
        session.delete(client_car)
        session.commit()
        return client_car_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Client with id {client_id} not found!")

