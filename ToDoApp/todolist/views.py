from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import FormToDoList
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def todoview(req):
    if req.method=='POST':
        forms=FormToDoList(req.POST or None)

        if forms.is_valid():
            # imp
            inst=forms.save(commit=False)
            inst.user=req.user
            inst.save()

    login_forms=AuthenticationForm()
    if req.user.is_authenticated:
        todo_list=ToDoList.objects.filter(user=req.user)
    else:
        todo_list=None
    return render(req, 'todolist/index.html', {'todo_list': todo_list, 'login_forms':login_forms})

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