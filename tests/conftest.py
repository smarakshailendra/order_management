import pytest
import os

from app import app as test_app
from app import db


@pytest.fixture
def client():
    test_app.config['TESTING'] = True
    test_app.config['WTF_CSRF_ENABLED'] = False
    client = test_app.test_client()
    with test_app.app_context():
        db.create_all()
    
    yield client
    
    with test_app.app_context():
        db.session.remove()
        db.drop_all()

