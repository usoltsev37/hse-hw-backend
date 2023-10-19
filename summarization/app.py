"""Module with main FastAPI application"""
from fastapi import FastAPI
from endpoints import router

app = FastAPI(
    title="Text Summarization model - bart-large-cnn",
    description=("Homework 3"),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)

app.include_router(router)