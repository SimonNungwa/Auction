import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<html' in response.data  # crude check for HTML content

def test_about_route(client):
    response = client.get('/about')
    assert response.status_code == 200

def test_recover_route(client):
    response = client.get('/recover')
    assert response.status_code == 200

def test_signup_route(client):
    response = client.get('/signup')
    assert response.status_code == 200

def test_search_route(client):
    response = client.get('/search')
    assert response.status_code == 200

def test_services_route(client):
    response = client.get('/services')
    assert response.status_code == 200