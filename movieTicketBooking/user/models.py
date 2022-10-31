from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    customer = models.BooleanField(default=False)
    theatre = models.BooleanField(default=False)
    administrator = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username}'