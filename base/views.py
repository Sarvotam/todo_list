from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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