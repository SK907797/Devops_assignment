import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_get_programs():
    client = app.test_client()
    response = client.get('/programs')
    assert response.status_code == 200

def test_get_program():
    client = app.test_client()
    response = client.get('/program/Fat%20Loss%20(FL)')
    assert response.status_code == 200

def test_invalid_program():
    client = app.test_client()
    response = client.get('/program/Invalid')
    assert response.status_code == 404