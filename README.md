# order_management
Webserver with order invoice management

## Problem Statement 

```
Use any Python web framework and ORM that you find appropriate for this project. 

You can use any database system (PostgreSQL, MySQL, or even SQLite).

- The project will have 2 models: "Invoice" and "InvoiceItem". 
- They both must have a unique 'id' column as well as be relationship using a foreign key to the Invoice id on the InvoiceItem model, so the invoice items are linked to their parent invoice. 
- The invoice model should have a date as well. 
- The InvoiceItem model will have an integer column "units", a string column "description" and a numeric column "amount".
- Then utilize the classes/models you just created inside a web app built using any Python web framework to expose a single "POST" endpoint so that we can create an invoice via the exposed URL. 
- Add another "POST" endpoint to add an InvoiceItem. 
- Add also some endpoints to be able to GET the created data. We would prefer to see this as a RESTful API.
```

### Stack information
- Python: 3.11
- Web framework: Flask
- Orm: SqlAlchemy
- DB: sqlite

### Installation

```
Clone the repo with https://github.com/smarakshailendra/order_management.git
```
```
cd order_management/
```
```
python -m venv venv
```
```
source venv/bin/activate
```
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
export FLASK_APP=app.py
```
```
flask db init
```
```
flask db migrate -m "Migration"
```
```
flask db upgrade
```
```
flask run
```

### Endpoints
```
Create Invoice

POST /invoice

request body example:
{
    "items": [
        {
            "units": 1, "description": "abc", "amount": 15
        }
    ]
}

response example:
{
  "invoice_id": 3
}
```
```
Create Invoice items

POST /invoice/<invoice_id>/item

request body example:
{
    "units": 1, "description": "abc", "amount": 10
}

response example:
{
  "invoice_item_id": 3
}
```
```
List all Invoices

GET /invoice

response example:
{
    "date": "Wed, 25 Jan 2023 14:24:05 GMT",
    "id": 2,
    "invoice_items": [
      {
        "amount": "5.00",
        "description": "abc",
        "id": 2,
        "invoice_id": 2,
        "units": 1
      }
    ]
}
```

```
List all Invoice items

GET /items

response example:
[
  {
    "amount": "2.00",
    "description": "rice",
    "id": 1,
    "invoice_id": 1,
    "units": 2
  }
]
```

### Run functional tests

```
pytest .\tests
```