from django.shortcuts import render, redirect
from builtwith import *
from django.views.generic import View
from django.contrib import messages
import json
from django.views.generic import TemplateView
# Create your views here.
import whois


def index(request):
    return render(request, 'index.html', {
        'teste': 'teste'
    })


def busca(request):
    termo = request.GET.get('termourl')
    # termo = 'globo.com'
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Texto vazio')
        return redirect('index')

    if 'http' in termo:
        print('termo ok')
    else:
        termo = 'http://' + termo
        print(termo)
    responseb = builtwith(termo)
    charmander = whois.whois(termo)
    print(f'response: {responseb}')

    if bool(responseb):
        responseJson = json.dumps(responseb)
        return render(request, 'busca.html', {
            'nome': 'teste',
            'resposta': responseb,
            'whowho': charmander
        })
    else:
        return redirect('index')
