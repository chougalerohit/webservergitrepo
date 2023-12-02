from django.shortcuts import render
from django.http import HttpResponse



def index(r):
    return HttpResponse('<h1>Welcome to first web App</h1>')
