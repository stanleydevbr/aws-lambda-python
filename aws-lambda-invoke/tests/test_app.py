from chalice.test import Client
from app import app

event = {
    'nome': 'Lucas',
    'idade': 24
}

def test_index():
    with Client(app) as client:
        response = client.lambda_.invoke('invoke', event)
        assert response.payload == True
