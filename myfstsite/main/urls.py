from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index,name="index"),
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("<int:id>/delete/", views.delete, name="delete"),
    path("<int:id>/update/", views.update, name="update"),
    path("search/", views.search, name="search"),
]
