from django.db import models

# Create your models here.


class Todo(models.Model):
    content = models.CharField(max_length=100)
    date_added = models.DateField()
