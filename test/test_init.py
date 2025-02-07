import pytest
from app import create_app, db
from sqlalchemy import inspect

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()  

    yield app  

    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    
    return app.test_client()

def test_app_creation(app):
    assert app is not None
    assert app.config["TESTING"] is True

def test_database_creation(app):
    with app.app_context():
        inspector = inspect(db.engine) 
        tables = inspector.get_table_names()
        assert "todo" in tables  

