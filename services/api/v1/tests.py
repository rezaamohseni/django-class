from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class Test_api:
    
    def test_view_services(self):
        c = APIClient()
        url = 'http://127.0.0.1:8000/services/api/v1/services'
        response = c.get(url)
        assert response.status_code == 200
        