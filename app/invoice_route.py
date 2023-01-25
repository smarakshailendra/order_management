from app import db, app
from app.models import Invoice, InvoiceItem

from flask import request, jsonify

from datetime import datetime


@app.route('/invoice', methods=['POST'])
def create_invoice():
    data = request.get_json()
    date = datetime.now()
    invoice = Invoice(date=date)
    db.session.add(invoice)
    db.session.commit()

    item_details = data.get("items", [])
    for item in item_details:
        invoice_item = InvoiceItem(invoice_id=invoice.id,
                                   units=item['units'],
                                   description=item['description'],
                                   amount=item['amount'])
        db.session.add(invoice_item)
    db.session.commit()
    return jsonify({"invoice_id": invoice.id}), 201


@app.route('/invoice', methods=['GET'])
def get_invoices():
    invoices = Invoice.query.all()
    return jsonify(invoices)
