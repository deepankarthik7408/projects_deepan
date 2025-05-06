from django.db import models
from django.contrib.auth.models import User


class Table(models.Model, ):
    name = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.TextField(default="")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default="")

    color = models.TextField(default="")

    def __str__(self):
        return self.name
    

class Task(models.Model):
    name = models.TextField(default="")
    description = models.TextField(default="")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, default="")

    color = models.TextField(default="")

    def __str__(self):
        return self.name


