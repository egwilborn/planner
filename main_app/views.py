from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import TodoForm


from .models import List, Todo
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
    # need to make a variable with the modelform containing the information in the request
    form = TodoForm(request.POST)
    if form.is_valid():
        # make a model instance using the form variable
        # can't save it to DB yet since it doesn't have the list FK
        new_todo = form.save(commit=False)
        new_todo.list_id = list_id
        new_todo.save()
    return redirect('list_detail', pk=list_id)
