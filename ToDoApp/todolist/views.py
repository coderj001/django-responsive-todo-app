from django.shortcuts import render
from .models import ToDoList
# Create your views here.

def todoview(req):
    todo_list=ToDoList()
    return render(req, 'todolist/index.html', {'todo_list': todo_list})

def about(req):
    return render(req, 'todolist/about.html',{})