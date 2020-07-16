import json

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import PersonSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CreatePerson(APIView):
    serializer_class = PersonSerializer

    def post(self, request):
        json_data = json.loads(request.body)  # request.raw_post_data w/ Django < 1.4
        try:
            name = json_data['name']
            embeddings = json_data["embeddings"]

            data = {'name': name, 'embeddings': embeddings}
            serializer = PersonSerializer(data=json_data)
            if serializer.is_valid():
                person = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
