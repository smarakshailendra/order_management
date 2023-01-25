import json
from tests.test_data import invoice_data


def test_create_invoice(client):
    
    response = client.post('/invoice', data=json.dumps(invoice_data), content_type='application/json')
    
    assert response.status_code == 201
    assert json.loads(response.data) == {"invoice_id": 1}


def test_get_invoice(client):
    client.post('/invoice', data=json.dumps(invoice_data), content_type='application/json')
    
    response = client.get('/invoice')

    assert response.status_code == 200

    data = json.loads(response.data)
    assert len(data) == 1