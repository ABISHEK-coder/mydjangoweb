from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def abi(request):
    return HttpResponse('<h1>helo welcome to the web</h2>')

def abishek(request):
    return HttpResponse('<h1>YOUR CONTACTS</h2>')

def abisheks(request):
    return HttpResponse('<h1>ABOUT</h2>')