"""Module with models for application"""
from datetime import datetime

from pydantic import BaseModel


class Task(BaseModel):
    """ Task of to-do list """
    name: str
    description: str = ""
    is_complete: bool = False
    deadline: datetime = None
