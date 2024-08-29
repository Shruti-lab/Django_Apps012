from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.

def index(request):
    return HttpResponse(f"<h1>datetime.datetime.now()</h1>")
