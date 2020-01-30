from django.shortcuts import render, redirect
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

def checkOff(req, list_id):
    todo_list=ToDoList.objects.get(pk=list_id)
    todo_list.status=False
    todo_list.save()
    return redirect('index')

def checkOn(req, list_id):
    todo_list=ToDoList.objects.get(pk=list_id)
    todo_list.status=True
    todo_list.save()
    return redirect('index')

def delete(req, list_id):
    todo_list=ToDoList.objects.get(pk=list_id)
    todo_list.delete()
    return redirect('index')