import pytest
from app.models import db, Todo

def test_add_todo(client, app):
    response = client.post("/", data={"title": "Test Task", "desc": "Test Description"})
    assert response.status_code == 200  

    with app.app_context():
        task = Todo.query.filter_by(title="Test Task").first()
        assert task is not None
        assert task.desc == "Test Description"

def test_fetch_todos(client, app):
    with app.app_context():
        task = Todo(title="Test Task", desc="Test Description")
        db.session.add(task)
        db.session.commit()

    response = client.get("/")
    assert response.status_code == 200
    assert b"Test Task" in response.data 

def test_delete_todo(client, app):
    
    with app.app_context():
        task = Todo(title="Delete Task", desc="To be deleted")
        db.session.add(task)
        db.session.commit()
        task_id = task.sno  

    response = client.get(f"/delete/{task_id}")
    assert response.status_code == 302  

    with app.app_context():
        deleted_task = Todo.query.filter_by(sno=task_id).first()
        assert deleted_task is None  
