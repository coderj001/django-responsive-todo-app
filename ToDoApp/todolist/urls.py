from django.urls import path
from . import views

app_name='todolist'

urlpatterns=[
    path('', views.todoview, name='todoview'),
    path('about/', views.about, name='about'),
    path('checkoff/<list_id>', views.checkOff, name='checkoff'),
    path('checkon/<list_id>',views.checkOn, name='checkon'),
    path('delete/<list_id>', views.delete, name='delete'),
]