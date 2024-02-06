from django.urls import path
from . import  views

urlpatterns = [
    path('', views.app1, name="app1"),
    path('souvik', views.souvik, name="souvik"),
    path("<str:name>", views.name, name="name"),
]