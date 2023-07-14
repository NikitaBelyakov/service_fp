
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from endpoints import car_router, client_router, client_car_router
from database import get_session


app = FastAPI()
app.include_router(car_router)
app.include_router(client_router)
app.include_router(client_car_router)
if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=5000,
                log_level="info",
                reload=True)
