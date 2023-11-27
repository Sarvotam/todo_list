from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#To create view we need to import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
# Create your views here.

# from django.http import HttpResponse

#Function based views
# def tasklist(request):
#     return HttpResponse('To Do List')

#Class base views
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks' #More readabale and better than just Object list [<!-- {% for task in object_list %} --> ]

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'
    
#By default this view looks for a template the model name and then the prefix(task) of underscore _form
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

#By default this view also looks for a template the model name and then the prefix(task) of underscore _form
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
