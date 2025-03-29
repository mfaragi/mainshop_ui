from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class MyToken(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    server_user_id = models.PositiveIntegerField(unique=True,null=True)
    token=models.CharField(max_length=500,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)