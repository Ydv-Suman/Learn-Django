from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.

def homepage(request):
    return HttpResponse({"Hello World from Django Backend"})