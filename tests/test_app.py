import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Flask CRUD App" in response.data

def test_add_item(client):
    response = client.post('/add', data={'name': 'Test', 'description': 'Sample item'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test' in response.data

def test_delete_nonexistent_item(client):
    response = client.get('/delete/nonexistent-id', follow_redirects=True)
    assert response.status_code == 200
