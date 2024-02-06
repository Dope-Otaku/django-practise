from . import views
from django.urls import path

urlpatterns = [
    path('', views.todo, name="todoapp"),
    path("add", views.add, name="addTask")
]