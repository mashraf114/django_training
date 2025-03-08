from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
  return HttpResponse("This ewewfwefworkss!")

def february(request):
  return HttpResponse("hello from feb!")