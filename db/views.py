from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Person

def db_list(request):
    people = Person.objects.all()
    data = {"results": list(people.values("id", "name", "embeddings"))}
    return JsonResponse(data)


def db_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    data = {"results": {
        "id": person.id,
        "name": person.name,
        "embeddings": person.embeddings
    }}
    return JsonResponse(data)
