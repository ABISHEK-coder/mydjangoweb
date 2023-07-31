from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
      return HttpResponse('<h1>WELCOME TO THE CHATS</h1>')
     
def yourchats(request):
      return HttpResponse('<h1>your chats</h1>')

def status(request):
      return HttpResponse('<h1>status</h1>')           