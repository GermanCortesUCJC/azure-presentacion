import azure.functions as func
from fastapi import FastAPI

fastapi_app = FastAPI(title="API de presentacion")


@fastapi_app.get("/api/health")
def health():
    return {"status": "ok"}


@fastapi_app.get("/api/saludo")
def saludo():
    return {"mensaje": "Hola desde Azure Functions + FastAPI"}


app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)
