from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("A view index funcionou, WOW!")
def sobre(request):
    return HttpResponse("A view sobre funcionou, WOW!")
def contato(request):
    return HttpResponse("Esta página é a de contato")
def ajuda(request):
    return HttpResponse("Esta é a página de ajuda")