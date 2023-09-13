from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import TodoForm


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


class ListDetail(DetailView):
    model = List

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_form"] = TodoForm
        return context


def todo_create(request, list_id):
    render()
