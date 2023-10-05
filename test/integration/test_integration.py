"""Module with integration tests"""
from datetime import datetime

from fastapi.testclient import TestClient

from database import database

from app import app
from model.task import Task

client = TestClient(app)


def test_add_complete():
    database.database.dictionary = {}

    task_name = "Homework 10"
    _ = client.post("add_task/", json={
        "name": task_name,
        "description": "Create FastAPI app",
        "is_complete": False,
        "deadline": str(datetime(2023, 10, 14, 23, 59))
    })

    assert database.database.dictionary[task_name].is_complete is False

    response = client.put(f"complete_task/{task_name}")
    assert response.json()["status_code"] == 200
    assert database.database.dictionary[task_name].is_complete


def test_add_complete_filter():
    database.database.dictionary = {}

    task_name = "Homework 11"
    _ = client.post("add_task/", json={
        "name": task_name,
        "description": "Create FastAPI app",
        "is_complete": False,
        "deadline": str(datetime(2023, 10, 14, 23, 59))
    })

    response = client.get(f"filter_tasks_by_complete/{False}")
    assert response.json()["status_code"] == 200
    assert len(response.json()["result"]) == 1
    response = client.get(f"filter_tasks_by_complete/{True}")
    assert response.json()["status_code"] == 200
    assert len(response.json()["result"]) == 0

    response = client.put(f"complete_task/{task_name}")
    assert response.json()["status_code"] == 200

    response = client.get(f"filter_tasks_by_complete/{True}")
    assert response.json()["status_code"] == 200
    assert len(response.json()["result"]) == 1


def test_add_filter():
    database.database.dictionary = {}

    task1 = Task(
        name="Homework3",
        description="",
        is_complete=True,
        deadline=datetime(2023, 11, 30, 23, 59)
    )
    _ = client.post("add_task/", json={
        "name": task1.name,
        "description": task1.description,
        "is_complete": task1.is_complete,
        "deadline": str(task1.deadline)
    })

    task2 = Task(
        name="Homework4",
        description="",
        is_complete=False,
        deadline=datetime(2023, 10, 14, 23, 59)
    )
    _ = client.post("add_task/", json={
        "name": task2.name,
        "description": task2.description,
        "is_complete": task2.is_complete,
        "deadline": str(task2.deadline)
    })

    response = client.get(f"filter_tasks_by_date/{str(datetime(2023, 10, 16, 23, 59))}")
    assert response.json()["status_code"] == 200
    assert len(response.json()["result"]) == 1
