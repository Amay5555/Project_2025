import pytest
from app.models import Todo
from app import db
from datetime import datetime, timezone

def test_create_todo(app):
    
    with app.app_context():
        
        task = Todo(title="Test Task", desc="Test Description")

        db.session.add(task)
        db.session.commit()

        retrieved_task = Todo.query.first()

        assert retrieved_task is not None
        assert retrieved_task.title == "Test Task"
        assert retrieved_task.desc == "Test Description"
        assert isinstance(retrieved_task.date_created, datetime)

def test_repr_todo():
    task = Todo(sno=1, title="Sample Task", desc="Sample Desc")
    assert repr(task) == "1 - Sample Task"
