"""Module with main FastAPI application"""
from fastapi import FastAPI
from endpoints import router

app = FastAPI(
    title="Text Generation and Summarization model",
    description=("Homework 3"),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)
