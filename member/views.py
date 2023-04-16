from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    x = "blaaaaa"
    return HttpResponse("Hello more hello, world. You're at the members index." + x)