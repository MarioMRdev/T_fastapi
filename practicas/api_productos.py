from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"mensaje":"Bienvenido a la API de Productos"}