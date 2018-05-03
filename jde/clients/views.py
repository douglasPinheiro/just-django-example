from django.shortcuts import render
from django.views.generic import ListView
from clients.models import Client

# Create your views here.
class ClientList(ListView):
    model = Client