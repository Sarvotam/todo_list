from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Function based views
def tasklist(request):
    return HttpResponse('To Do List')
