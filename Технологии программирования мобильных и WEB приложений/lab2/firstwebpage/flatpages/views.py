from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django import template

# Create your views here.
def home(request):
    return HttpResponse(u'Hello World!')

def hello(request):
    return render(request, 'templates/static_handler.html')
