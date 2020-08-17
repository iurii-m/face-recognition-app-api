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

    print("Person added with the name:", name, "and embeddings:", embeddings)

    return custom_response({"name": name}, 200)


@person_api.route('/search', methods=['POST'])
def search_person():
    embeddings = request.json['embeddings']

    people = PersonModel.get_all_person()

    index = 0
    best_score = 0.0
    found = False
    for i, p in enumerate(people):
        found = True
        score = dot(embeddings, p.embeddings)/(norm(embeddings) * norm(p.embeddings))
        if score > best_score:
            index = i
            best_score = score

    if found:
        response = {"name": people[index].name, "score": best_score}
    else:
        response = {}
    return custom_response(response, 200)


@person_api.route('/all', methods=['GET'])
def get_all():
    people = PersonModel.get_all_person()
    all_people = person_schema.dump(people, many=True)
    return custom_response(all_people, 200)


@person_api.route('/delete', methods=['GET'])
def delete_all():
    number = PersonModel.delete_all()
    return custom_response(number, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
