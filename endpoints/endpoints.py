"""Module with endpoints for application"""
from datetime import datetime

from fastapi import APIRouter

from database.database import database
from model.task import Task

router = APIRouter()


@router.post("/add_task/")
async def add_task(task: Task):  # noqa: D103
    """
    Endpoint for adding task to database
    :param task: task for to-do list
    :return: json with status_code and detail
    """
    if task.name in database.dictionary.keys():
        return {"status_code": 400, "detail": f"You already have a task with this name: {task}"}
    database.dictionary[task.name] = task
    return {"status_code": 200, "detail": "Success"}


@router.put("/complete_task/{name}")
async def complete_task(name: str):  # noqa: D103
    """
    Endpoint for completing task from database
    :param name: name of the task
    :return: json with status_code and detail
    """
    if name not in database.dictionary.keys():
        return {"status_code": 400, "detail": "The task does not exist in the database"}
    if database.dictionary[name].is_complete:
        return {"status_code": 400, "detail": "The task was already complete"}
    database.dictionary[name].is_complete = True
    return {"status_code": 200, "detail": "Success"}


@router.get("/filter_tasks_by_complete/{is_complete}")
async def filter_tasks_by_complete(is_complete: bool):  # noqa: D103
    """
    Endpoint for filtering tasks from database by is_complete condition
    :param is_complete: True for getting completed tasks / False for getting not completed tasks
    :return: json with status_code and result
    """
    result = list(filter(lambda t: t.is_complete == is_complete, database.dictionary.values()))
    return {"status_code": 200, "result": result}


@router.get("/filter_tasks_by_date/{date}")
async def filter_tasks_by_date(date: datetime):  # noqa: D103
    """
    Endpoint for filtering tasks from database by deadline condition
    :param date: tasks with a deadline before this date
    :return: json with status_code and result
    """
    result = list(filter(
        lambda t: t.deadline is not None and t.deadline < date, database.dictionary.values()
    ))
    return {"status_code": 200, "result": result}
