from django.db import models
# Create your models here.
class Register(models.Model):
    userId=models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=200,default="")
    lastName=models.CharField(max_length=200,default="")
    Email=models.CharField(max_length=200,default="")
    password=models.CharField(max_length=200,default="")
    Image=models.CharField(max_length=200,default="")
    gender=models.CharField(max_length=200,default="")

    isActive=models.BooleanField(default=True)

