from fastapi import FastAPI

api = FastAPI()


@api.get("/")
def index():
    data = {"status": 200, "message": "Hola Mundo"}
    return data


def app():
    return api
