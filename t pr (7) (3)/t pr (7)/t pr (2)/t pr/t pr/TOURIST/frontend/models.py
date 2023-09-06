from django.db import models

# Create your models here.
class sign_indb(models.Model):
    username=models.CharField(max_length=30, null=True, blank=True)
    email= models.EmailField(max_length=30, null=True, blank=True)
    password=models.CharField(max_length=30, null=True, blank=True)
    cpassword=models.CharField(max_length=30, null=True, blank=True)
class reservationdb(models.Model):
    user = models.CharField(max_length=30, null=True, blank=True)
    Name = models.CharField(max_length=100,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    Guests = models.IntegerField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    Destination = models.CharField(max_length=100,null=True,blank=True)


class transactiondb(models.Model):
    cardnumber = models.IntegerField(null=True,blank=True)
    monthyear = models.CharField(max_length=100,null=True,blank=True)
    cvvcode = models.IntegerField(null=True,blank=True)
    cardname = models.CharField(max_length=100,null=True,blank=True)
    amount = models.IntegerField(null=True, blank=True)