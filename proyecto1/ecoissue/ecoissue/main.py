from fastapi import FastAPI
from datetime import datetime

api = FastAPI()


@api.get("/")
def index():
    data = {"status": 200, "message": "Hola Mundo"}
    return data

@api.get('/marcaciones')
def marcaciones():
    return {"usuario":1111, "hora":datetime.utcnow() }

def app():
    return api
