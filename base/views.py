from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#To create view we need to import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#https://ccbv.co.uk/projects/Django/4.2/django.contrib.auth.views/LoginView/
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fileds = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

# from django.http import HttpResponse

#Function based views
# def tasklist(request):
#     return HttpResponse('To Do List')

#Class base views
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks' #More readabale and better than just Object list [<!-- {% for task in object_list %} --> ]

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    
#By default this view looks for a template the model name and then the prefix(task) of underscore _form
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

#By default this view also looks for a template the model name and then the prefix(task) of underscore _form
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


