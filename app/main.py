from fastapi import FastAPI
from app import routes

app = FastAPI(title="FastAPI CI Project")

app.include_router(routes.router)
