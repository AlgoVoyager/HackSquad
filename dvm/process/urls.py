from django.urls import path
from . import views

urlpatterns = [

    path("vote/", views.verify, name="verify"),
    path("", views.index, name="index"),
    path("submitted/", views.vote, name="vote"),
    path("results/", views.results, name="results"),


]
