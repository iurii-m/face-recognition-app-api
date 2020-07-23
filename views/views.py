from flask import json, Response, Blueprint, request
from numpy import dot
from numpy.linalg import norm

from models.models import PersonSchema, PersonModel

person_api = Blueprint('Person', __name__)
person_schema = PersonSchema()


@person_api.route('/add', methods=['POST'])
def add_person():
    embeddings = request.json['embeddings']
    name = request.json['name']

    person = PersonModel(name, embeddings)
    person.save()

    print("Person added with the name:", name)

    return custom_response({"name": name}, 202)


@person_api.route('/search', methods=['POST'])
def search_person():
    embeddings = request.json['embeddings']

    people = PersonModel.get_all_person()

    index = 0
    best_score = 0.0
    for i, p in enumerate(people):
        score = dot(embeddings, p.embeddings)/(norm(embeddings) * norm(p.embeddings))
        if score > best_score:
            index = i
            best_score = score

    response = {"name": people[index].name, "score": best_score}
    return custom_response(response, 200)


@person_api.route('/all', methods=['GET'])
def get_all():
    people = PersonModel.get_all_person()
    all_people = person_schema.dump(people, many=True)
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
