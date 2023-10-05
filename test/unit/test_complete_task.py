"""Module with tests for complete_task endpoint"""
from fastapi.testclient import TestClient
from database import database

from app import app
from model.task import Task

client = TestClient(app)


def test_correct_task():
    task = Task(
        name="Homework03",
        description="",
        is_complete=False
    )
    database.database.dictionary[task.name] = task

    response = client.put(f"complete_task/{task.name}")
    assert response.json()["status_code"] == 200
    assert database.database.dictionary[task.name].is_complete


def test_completed_task():
    task = Task(
        name="Homework03",
        description="",
        is_complete=True
    )
    database.database.dictionary[task.name] = task

    response = client.put(f"complete_task/{task.name}")
    assert response.json()["status_code"] == 400
    assert database.database.dictionary[task.name].is_complete


def test_out_of_db_task():
    name = "Homework Mock"

    response = client.put(f"complete_task/{name}")
    assert response.json()["status_code"] == 400
    assert name not in database.database.dictionary.keys()
