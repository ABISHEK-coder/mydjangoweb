from django.shortcuts import render
import datetime 
# Create your views here.

def home(request):
   date = datetime.datetime.now()
   date_dirt = {'home_date':date}
   return render (request,'tempapp/index.html',context=date_dirt)

def contact(request):
    return render(request,'tempapp/contact.html')