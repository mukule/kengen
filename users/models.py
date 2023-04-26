from django.contrib.auth.models import AbstractUser
from django.db import models
import os

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    
    def __str__(self):
        return self.username
    
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Users', self.username, instance)
        return None

    image = models.ImageField(default='default/user.png', upload_to=image_upload_to)
