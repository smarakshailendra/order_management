from app import db, app
from app.models import Invoice, InvoiceItem

from flask import request, jsonify

from datetime import datetime


@app.route('/invoice/<invoice_id>/item', methods=['POST'])
def create_invoice_item(invoice_id):
    data = request.get_json()
    invoice = Invoice.query.filter_by(id=invoice_id).first()
    if invoice is None:
        return jsonify({"error": "Invoice not found"}), 404
    invoice_item = InvoiceItem(invoice_id=invoice.id,
                               units=data['units'],
                               description=data['description'],
                               amount=data['amount'])
    db.session.add(invoice_item)
    db.session.commit()
    return jsonify({"invoice_item_id": invoice_item.id}), 201


@app.route('/invoice', methods=['GET'])
def get_invoices():
    invoices = Invoice.query.all()
    return jsonify(invoices)


@app.route('/items', methods=['GET'])
def get_invoice_items():
    items = InvoiceItem.query.all()
    return jsonify(items)
