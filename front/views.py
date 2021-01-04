from django.shortcuts import render, redirect
from builtwith import *
from django.views.generic import View

from django.views.generic import TemplateView
# Create your views here.


# def index(request):
#     return render(request, 'index.html', {
#         'teste': 'teste'
#     })


def busca(request):
    # termo = request.GET.get('termourl')
    termo = 'globo.com'
    if 'http' in termo:
        print('oi')
    else:
        termo = 'http://' + termo
        print(termo)
    responseb = builtwith(termo)
    print(f'response: {responseb}')


busca('a')
