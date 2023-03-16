from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import socket

def index(request):
    host_name=socket.gethostname()
    return HttpResponse(f"WELCOME TO HOME PAGE,THIS IS HOSTED ON CONTAINER ID {host_name}")
    
