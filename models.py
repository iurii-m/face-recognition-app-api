from marshmallow import fields, Schema

from app import db


class PersonModel(db.Model):
    """
    Person Model
    """

    __tablename__ = 'Person'

    id_person = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    embeddings = db.Column(db.ARRAY(db.Float, dimensions=512), nullable=False)

    def __init__(self, data):
        self.name = data.get('name')
        self.embeddings = data.get('embeddings')

    @staticmethod
    def get_all_person():
        return PersonModel.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_user_by_name(name):
        return PersonModel.query.filter_by(name=name).first()

    @staticmethod
    def get_one_person(id):
        return PersonModel.query.get(id)


class RelationsSchema(Schema):
    """
    Blogpost Schema
    """
    id_recipe = fields.Int(dump_only=True)
    id_ingredient = fields.Int(dump_only=True)
