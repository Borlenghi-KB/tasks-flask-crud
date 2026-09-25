import pytest
import requests

#Crud
Base_URL = "http://localhost:5000"
tasks = []

def test_create_task():
    data = {
        "title": "Test Task",
        "description": "This is a test task.",
        "completed": False
    }
    response = requests.post(f"{Base_URL}/tasks", json=data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])  


def test_get_tasks():
    response = requests.get(f"{Base_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json
    assert isinstance(response_json["tasks"], list)
    assert isinstance(response_json["total_tasks"], int)

def test_get_task():
    if not tasks:
        pytest.skip("No tasks available to test.")
    task_id = tasks[0]
    response = requests.get(f"{Base_URL}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert task_id == response_json["id"]

def test_update_task():
    if tasks:
        task_id = tasks[0]
        data = {
            "title": "Updated Test Task",
            "description": "This is an updated test task.",
            "completed": True
        }
        response = requests.put(f"{Base_URL}/tasks/{task_id}", json=data)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        #Nova requisição

        response = requests.get(f"{Base_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == data["title"]
        assert response_json["description"] == data["description"]
        assert response_json["completed"] == data["completed"]


def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{Base_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        #Nova requisição para verificar se a tarefa foi deletada
        response = requests.get(f"{Base_URL}/tasks/{task_id}")
        assert response.status_code == 404