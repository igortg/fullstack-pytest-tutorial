import pytest
from flask import json

from toh.model import db
from toh.app import app, init_app


@pytest.fixture(scope='session')
def client():
    init_app(app)
    test_client = app.test_client()
    with app.app_context():
        yield test_client


@pytest.fixture(scope='session')
def db_engine(client):
    '''
    Setup the database for a test session and drop all tables
    after the session ends. It is not intended to be used on
    tests functions, use `db_session` instead.
    '''
    db.create_all()
    yield db.engine
    db.drop_all()


@pytest.yield_fixture(scope='function')
def db_session(db_engine):
    '''
    Creates a new database transaction for the test and roll it back
    when the test is completed
    '''
    connection = db_engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    yield session

    db.session.close()
    transaction.rollback()
    connection.close()
