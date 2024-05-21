from django.db import models
from django.contrib.auth.models import User

class UserInfo (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=30, default=None)
    about = models.CharField(max_length=300)
    job = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    fb_profile = models.CharField(max_length=30)
    inst_profile = models.CharField(max_length=30)
    link_profile = models.CharField(max_length=30)
    tw_profile = models.CharField(max_length=30)
    image = models.ImageField(upload_to= 'image', default=None,null=True) 
    