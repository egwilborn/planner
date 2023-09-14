from django.db import models
from django.urls import reverse
# Create your models here.


class List(models.Model):
    title = models.CharField(max_length=50)
    date_made = models.DateField("Date Started")

    def get_absolute_url(self):
        return reverse('list_detail', kwargs={'pk': self.id})


class Todo(models.Model):
    content = models.CharField(max_length=100)
    date_added = models.DateField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)
