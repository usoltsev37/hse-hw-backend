"""Module with entrypoints for FastAPI application"""
from fastapi import APIRouter
from db import list_visitor_names
from model import Visitor

router = APIRouter()


@router.get("/")
def hello_root():  # noqa: D103
    """
    Root entrypoint with constant Hello World
    :return: json with Hello World
    """
    return {"Hello": "World"}


@router.get("/{name}")
async def hello_person(name: str):  # noqa: D103
    """
    Entrypoint with Hello :param name. Greets a person by name
    and remembers the name in the list of visitors
    :param name: name of the user
    :return: json with the greeting of a person by name
    """
    list_visitor_names.append(name)
    return {"Hello": f"{name}!"}


@router.post("/is_visitor/")
async def is_visitor(visitor: Visitor):  # noqa: D103
    """
    Entrypoint with a check whether this visitor has visited our service
    :param visitor: Visitor of the service
    :return: bool: True if the Visitor has already been in our service
    """
    return {"result": f"{visitor.name in list_visitor_names}"}
