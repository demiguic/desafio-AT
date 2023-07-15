from django.shortcuts import render
import requests
from yahoo_fin import stock_info as si


# Create your views here.


def login(request):
    return render(request, 'login.html')


def acoes(request, user):

    return render(request, 'list.html', {'user': user})
