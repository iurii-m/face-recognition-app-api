from flask import json, Response, Blueprint
from models.models import PersonSchema, PersonModel

person_api = Blueprint('Person', __name__)
person_schema = PersonSchema()


@person_api.route('/add', methods=['POST'])
def add_person():
    return "Add endpoint"


@person_api.route('/get/<list:embeddings>', methods=['GET'])
def search_person(embeddings):
    return "Embeddings endpoint"


@person_api.route('/all', methods=['GET'])
def get_all():
    people = PersonModel.get_all_person()
    all_people = person_schema.dump(people, many=True).data
    return custom_response(all_people, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
