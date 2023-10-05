"""Module with tests for filter endpoints"""
from datetime import datetime

from fastapi.testclient import TestClient

from database import database

from app import app
from model.task import Task

client = TestClient(app)


def test_correct_request():
    database.database.dictionary = {}

    task = Task(
        name="Homework03",
        description="",
        is_complete=False
    )
    database.database.dictionary[task.name] = task

    response = client.get(f"filter_tasks_by_complete/{False}")
    assert response.json()["status_code"] == 200
    assert len(response.json()["result"]) == 1
    assert response.json()["result"][0]['name'] == task.name


def test_empty_result():
    database.database.dictionary = {}

    task1 = Task(
        name="Homework03",
        description="",
        is_complete=False
    )
    database.database.dictionary[task1.name] = task1

    task2 = Task(
        name="Homework04",
        description="",
        is_complete=False
    )
    database.database.dictionary[task2.name] = task2

    response = client.get(f"filter_tasks_by_complete/{True}")
    assert response.json()["status_code"] == 200
    assert len(response.json()["result"]) == 0


def test_date():
    database.database.dictionary = {}

    task1 = Task(
        name="Homework03",
        description="",
        is_complete=False
    )
    database.database.dictionary[task1.name] = task1

    task2 = Task(
        name="Homework04",
        description="",
        is_complete=False,
        deadline=datetime(2023, 10, 14, 23, 59)
    )
    database.database.dictionary[task2.name] = task2

    response = client.get(f"filter_tasks_by_date/{str(datetime(2023, 10, 29, 23, 59))}")
    assert response.json()["status_code"] == 200
    assert len(response.json()["result"]) == 1


def test_date_empty():
    database.database.dictionary = {}

    task1 = Task(
        name="Homework03",
        description="",
        is_complete=False,
        deadline=datetime(2024, 4, 30, 23, 59)
    )
    database.database.dictionary[task1.name] = task1

    task2 = Task(
        name="Homework04",
        description="",
        is_complete=False,
        deadline=datetime(2023, 10, 14, 23, 59)
    )
    database.database.dictionary[task2.name] = task2

    response = client.get(f"filter_tasks_by_date/{str(datetime(2023, 9, 29, 23, 59))}")
    assert response.json()["status_code"] == 200
    assert len(response.json()["result"]) == 0
