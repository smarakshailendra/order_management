import json
from tests.test_data import invoice_data, item_data


def test_add_invoice_item(client):
    
    response = client.post('/invoice', data=json.dumps(invoice_data), content_type='application/json')
    
    assert response.status_code == 201
    assert json.loads(response.data) == {"invoice_id": 1}

    response = client.post('/invoice/1/item', data=json.dumps(item_data), content_type='application/json')
    assert response.status_code == 201
    assert json.loads(response.data) == {"invoice_item_id": 3}


def test_get_invoice_item(client):
    client.post('/invoice', data=json.dumps(invoice_data), content_type='application/json')
    client.post('/invoice/1/item', data=json.dumps(item_data), content_type='application/json')

    response = client.get('/items')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert len(data) == 3