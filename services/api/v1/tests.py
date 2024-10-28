from rest_framework.test import APIClient
import pytest

#set global 
@pytest.fixture
def client():
    c = APIClient()
    return c

@pytest.mark.django_db

class Test_api:
    
    def test_view_services(self , client):
        url = 'http://127.0.0.1:8000/services/api/v1/services'
        response = client.get(url)
        assert response.status_code == 200
        
    def test_create_object_on_services(self):
        data = {
            "name": "test1",
            "title" : "test2",
            "content" : "test3",
            "description" : "test4",
            "price" : 200,
        }
        c = APIClient()
        url = "http://127.0.0.1:8000/services/api/v1/services"
        response = c.post(url , data)
        assert response.status_code == 201
        