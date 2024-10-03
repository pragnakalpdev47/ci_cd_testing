import pytest
# from app import app

# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_form_page(client):
    """Test that the form page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Submit" in response.data

def test_success_page(client):
    """Test that the success page is displayed after form submission."""
    response = client.post("/", data={"name": "Test User", "email": "test@example.com", "password": "password123"})
    assert response.status_code == 302  # Redirect to success page
    follow_response = client.get("/success")
    assert b"Success" in follow_response.data
