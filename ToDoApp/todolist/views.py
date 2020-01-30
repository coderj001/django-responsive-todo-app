from django.shortcuts import render
from .models import ToDoList
from .forms import FormToDoList

# Create your views here.

def todoview(req):
    if req.method=='POST':
        forms=FormToDoList(req.POST or None)
        if forms.is_valid():
            forms.save()

    todo_list=ToDoList.objects.all()
    return render(req, 'todolist/index.html', {'todo_list': todo_list})

def about(req):
    return render(req, 'todolist/about.html',{})