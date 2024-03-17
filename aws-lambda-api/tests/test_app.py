from chalice.test import Client
from app import app


def test_index():
    with Client(app) as client:
        response = client.http.get('/id/993838')
        assert response.json_body == True
