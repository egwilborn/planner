from django.db import models

# Create your models here.


class Todo(models.Model):
    content = models.CharField(max_length=100)
    date_added = models.DateField()


class List(models.Model):
    title = models.CharField(max_length=50)
    date_made = models.DateField("Date Started")
