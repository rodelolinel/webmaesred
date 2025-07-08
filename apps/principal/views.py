from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

cliente = 'Maes Colombia SAS'
usuario = 'Linel Rodelo'
slogan = 'Nuestra ganancia es su confianza'


# Create your views here.
def principal(request):
    data = {
        'titulo': 'MaesRed Colombia SAS',
        'cliente': 'Linel Rodelo',
        'cargo': 'operaciones',
    }

    return render(request, "maesred.html", data)
