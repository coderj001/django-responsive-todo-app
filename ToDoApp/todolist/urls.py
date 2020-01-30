from django.urls import path
from . import views

app_name='todolist'

urlpatterns=[
    path('', views.todoview, name='todoview'),
]