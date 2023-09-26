"""Module with main FastAPI application"""
from fastapi import FastAPI
from routers import router

app = FastAPI(
    title="Homework1",
    description=("Homework 1"),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)
