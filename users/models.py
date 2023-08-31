from django.contrib.auth.models import AbstractUser
from django.db import models
import os

class CustomUser(AbstractUser):
    SYSTEM_ADMIN = 'system_admin'
    SUPER_ADMIN = 'super_admin'
    STAFF = 'staff'
    
    ACCESS_LEVEL_CHOICES = (
         (STAFF, 'staff'),
        (SYSTEM_ADMIN, 'System Admin'),
        (SUPER_ADMIN, 'Super Admin'),
    )
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    access_level = models.CharField(max_length=20, choices=ACCESS_LEVEL_CHOICES, default=STAFF)

    def __str__(self):
        return f"{self.username} ({self.get_access_level_display()})"

    def image_upload_to(self, instance=None, filename=None):
        if instance and filename:
            return os.path.join('Users', self.username, filename)
        return None

    image = models.ImageField(default='default/user.png', upload_to=image_upload_to)