import pytest
import requests
 
@pytest.fixture
def test_home_page():
    response = requests.get("http://localhost:8080/")
    assert response.status_code == 200