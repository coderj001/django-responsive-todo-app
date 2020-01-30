from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(req):
    if req.method == "POST":
        froms=UserCreationForm(req.POST)
        if froms.is_valid:
            user=froms.save()
            login(req,user)
            return redirect('todolist:todoview')
        return render(req, 'account/signup.html', {'forms':froms})
    else:
        forms=UserCreationForm()
        return render(req, 'account/signup.html', {'forms':forms})

def login_view(req):
    if req.method == "POST":
        forms=AuthenticationForm(data=req.POST)
        if forms.is_valid():
            # login
            user=forms.get_user()
            login(req, user)
    return redirect('index')


def logout_view(req):
    if req.user.is_authenticated:
        logout(req)
    return redirect('index')