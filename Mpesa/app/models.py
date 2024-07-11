# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
from app import db

class BaseModel(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class MpesaCalls(BaseModel):
    id = db.Column(db.BigInteger, primary_key=True)
    ip_address = db.Column(db.Text)
    caller = db.Column(db.Text)
    conversation_id = db.Column(db.Text)
    content = db.Column(db.Text)

class MpesaCallBacks(BaseModel):
    id = db.Column(db.BigInteger, primary_key=True)
    ip_address = db.Column(db.Text)
    caller = db.Column(db.Text)
    conversation_id = db.Column(db.Text)
    content = db.Column(db.Text)

class MpesaPayment(BaseModel):
    id = db.Column(db.BigInteger, primary_key=True)
    amount = db.Column(db.Numeric(10, 2))
    description = db.Column(db.Text)
    type = db.Column(db.Text)
    reference = db.Column(db.Text)
    first_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone_number = db.Column(db.Text)

    def __str__(self):
        return self.first_name
