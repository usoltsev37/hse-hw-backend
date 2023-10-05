"""Module with main FastAPI application"""
from fastapi import FastAPI
from endpoints.endpoints import router

app = FastAPI(
    title="TO-DO list",
    description=("Homework 2"),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)
