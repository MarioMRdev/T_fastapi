from typing import Union
from fastapi import FastAPI

# Creación de una aplicación en FastAPI:

app = FastAPI()

@app.get("/")
def road_root():
    return {"Hello": "World!"}

@app.get("/hola")
def hola_mundo():
    return {"Hola": "Mundo"}