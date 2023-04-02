from marshmallow import Schema, fields
from app.database import db


class Document(db.Model):
    __tablename__ = "document"

    id = db.Column(db.Integer, primary_key=True)
    rubrics = db.Column(db.String(100))
    text = db.Column(db.String(500))
    created_date = db.Column(db.Date)


class DocumentSchema(Schema):
    id = fields.Int()
    rubrics = fields.Str()
    text = fields.Str()
    created_date = fields.Date()
