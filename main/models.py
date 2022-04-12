from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "list", null = True)
    name = models.CharField(max_length = 100, help_text = "Enter List Name")

    def __str__(self):
        return self.name

class Item(models.Model):
    completed = models.BooleanField()
    name = models.CharField(max_length = 200, help_text = "Enter Task")
    list = models.ForeignKey(List, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
