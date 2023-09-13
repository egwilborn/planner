from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


from .models import List
# Create your views here.


def home(request):
    return render(request, 'home.html')


class ListCreate(CreateView):
    model = List
    fields = '__all__'
    success_url = "/lists/"


class ListIndex(ListView):
    model = List
