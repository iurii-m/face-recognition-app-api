from django.urls import path
from .apiviews import PersonList, PersonDetail, CreatePerson

urlpatterns = [
    path("db/", PersonList.as_view(), name="db_list"),
    path("db/<int:pk>/", PersonDetail.as_view(), name="db_detail"),
    path("db/add/", CreatePerson.as_view(), name="create_person"),
]