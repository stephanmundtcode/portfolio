import pytest
from app.app import create_app
from os import environ

#database
from flask_migrate import upgrade

@pytest.fixture
def client():
    environ['DATABASE_URL'] = 'sqlite://'
    app = create_app()

    with app.app_context():
        upgrade()
        yield app.test_client()
