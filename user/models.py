from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class MyToken(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=500,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)