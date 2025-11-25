import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert b"Examen CI/CD" in rv.data
    assert rv.status_code == 200

def test_prediction_high(client):
    data = {'value': 80}
    rv = client.post('/predict', 
                     data=json.dumps(data), 
                     content_type='application/json')
    json_data = rv.get_json()
    assert json_data['prediction'] == 'Alto Impacto'

def test_prediction_low(client):
    data = {'value': 10}
    rv = client.post('/predict', 
                     data=json.dumps(data), 
                     content_type='application/json')
    json_data = rv.get_json()
    assert json_data['prediction'] == 'Bajo Impacto'