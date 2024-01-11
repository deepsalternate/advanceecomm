from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class person(models.Model):
    user=models.CharField(max_length=100)
    
    
#first creating custom user overridinng default login 
class CustomUser(AbstractUser):
    user_type_choices=((1,'Admin'),(2,'staff'),(3,"Merchant"),(4,"Customer"))
    user_type=models.Charfield(max_length=255,choices=user_type_choices,default=1)
    
class AdminUser(models.Model):
    profile_pic=models.FileField(default='')
    created_at=models.DateTimeField(auto_now_add=True)

class StaffUser(models.Model):
    profile_pic=models.Filefield(default='')
    created_at=models.DateTimeField(auto_now_add=True)
    
class MerchantUser(models.Model):
    profile_pic=models.Filefield(default='')
    company_name=models.CharField(max_length=255)
    gst_details=models.CharField(max_length=100)
    address=models.Textfield()
    created_at=models.DateTimeField(auto_now_add=True)
    
class CustomerUser(models.Model):
    profile_pic=models.Filefield(default='')
    created_at=models.DateTimeField(auto_now_add=True)   


#   CATEGORIES MODELS

class categories (models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    url_slug=models.CharField(max_length=255)
    thumbnail=models.FileField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    

