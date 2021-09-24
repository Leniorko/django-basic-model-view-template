from django.http import HttpResponse
from django.shortcuts import render
from .models import Client

# Create your views here.
from django.template.loader import get_template


def clientsIndex(request):
    clients = Client.objects.all()
    return render(request, "indexClients.html", {"clients": clients})

def clientPage(request, id):
    client = Client.objects.get(pk=id)
    return render(request, "clientPage.html", {"client": client})