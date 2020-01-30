from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    item=models.CharField(max_length=240)
    status=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item