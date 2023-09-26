"""Module with models for FastAPI application"""
from pydantic import BaseModel


class Visitor(BaseModel):
    """ Visitor of our service """
    name: str
