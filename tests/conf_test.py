import pytest
from app import create_flask_app
from dal.extensions import db


@pytest.fixture(scope="session")
def app():
    app = create_flask_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", # Base en mémoire pour isolation totale
    })

    db.init_app(app)
    with app.app_context():
        db.create_all()
    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()