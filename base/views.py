from django.shortcuts import render
from django.views.generic.list import ListView
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
