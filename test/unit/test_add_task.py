"""Module with tests for add_task endpoint"""
from datetime import datetime

from fastapi.testclient import TestClient

from database import database

from app import app

client = TestClient(app)


def test_correct_task():
    prev_database_size = len(database.database.dictionary.values())
    response = client.post("add_task/", json={
        "name": "Homework 01 - Python BackEnd",
        "description": "Create FastAPI app",
        "is_complete": False,
        "deadline": str(datetime(2023, 10, 14, 23, 59))
    })
    assert response.json()["status_code"] == 200
    assert response.json()["detail"] == "Success"
    assert len(database.database.dictionary.values()) == prev_database_size + 1


def test_exist_task():
    _ = client.post("add_task/", json={
        "name": "Homework 02",
        "description": "Create FastAPI app",
        "is_complete": False,
        "deadline": str(datetime(2023, 10, 14, 23, 59))
    })
    prev_database_size = len(database.database.dictionary.values())
    response = client.post("add_task/", json={
        "name": "Homework 02",
        "description": "-/-"
    })
    assert response.json()["status_code"] == 400
    assert len(database.database.dictionary.values()) == prev_database_size


def test_required_field():
    prev_database_size = len(database.database.dictionary.values())
    response = client.post("add_task/", json={
        "description": "Create FastAPI app",
        "is_complete": False,
        "deadline": str(datetime(2023, 10, 14, 23, 59))
    })
    assert len(database.database.dictionary.values()) == prev_database_size
    assert response.status_code == 422
