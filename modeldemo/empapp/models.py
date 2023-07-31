from django.db import models

# Create your models here.
class empapp(models.Model):
    nou = models.IntegerField()
    name = models.CharField(max_length=20)
    sal = models.IntegerField()
    address = models.CharField(max_length=50)

     