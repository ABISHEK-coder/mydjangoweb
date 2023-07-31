from django.shortcuts import render
from empapp.models import empapp
# Create your views here.
def  enm_detail(request):
    empdata= empapp.objects.all()
    emp_dict= {'emp_list':empdata}
    return render(request,'empapp/contact.html',context=emp_dict)