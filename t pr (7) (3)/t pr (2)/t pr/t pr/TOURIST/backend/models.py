from django.db import models

# Create your models here.
class categorydb(models.Model):
    country=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)

class productdb(models.Model):
     country=models.CharField(max_length=100,null=True,blank=True)
     place=models.CharField(max_length=100,null=True,blank=True)
     pricerange=models.CharField(max_length=100,null=True,blank=True)
     image=models.ImageField(upload_to="product",null=True,blank=True)
     description = models.CharField(max_length=100, null=True, blank=True)

