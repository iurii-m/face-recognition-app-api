from marshmallow import fields, Schema
from sqlalchemy.dialects.postgresql import ARRAY

from . import db


class PersonModel(db.Model):
    """
    Person Model
    """

    __tablename__ = 'Person'

    id_person = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    embeddings = db.Column(ARRAY(db.Float, dimensions=1), nullable=False)

    def __init__(self, name, embeddings):
        self.name = name
        self.embeddings = embeddings

    @staticmethod
    def get_all_person():
        return PersonModel.query.all()

    @staticmethod
    def delete_all():
        num_rows_deleted = db.session.query(PersonModel).delete()
        db.session.commit()
        return num_rows_deleted

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Person %r>' % self.name

    @staticmethod
    def get_user_by_name(name):
        return PersonModel.query.filter_by(name=name).first()

    @staticmethod
    def get_one_person(id):
        return PersonModel.query.get(id)


class PersonSchema(Schema):
    """
    Person Schema
    """
    name = fields.String(dump_only=True)
    embeddings = fields.String(dump_only=True)
