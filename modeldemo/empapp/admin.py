from django.contrib import admin
from empapp.models import empapp

# Register your models here.

class empadmin(admin.ModelAdmin):
    enm_detail = ['nou','name','sal','address']

admin.site.register(empapp)