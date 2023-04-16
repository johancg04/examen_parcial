from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def loginHTML(request):
    return render(request, 'login.HTML')
