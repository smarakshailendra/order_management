from app import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class InvoiceItem(db.Model):
    id: int
    invoice_id: int
    units: int
    description: str
    amount: float

    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer,
                           db.ForeignKey('invoice.id'),
                           nullable=False)
    units = db.Column(db.Integer)
    description = db.Column(db.String(255))
    amount = db.Column(db.Numeric(10, 2))


@dataclass
class Invoice(db.Model):
    id: int
    date: datetime
    invoice_items: InvoiceItem

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    invoice_items = db.relationship('InvoiceItem',
                                    backref='invoice',
                                    lazy=True)
