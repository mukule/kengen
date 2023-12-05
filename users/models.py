from django.contrib.auth.models import AbstractUser
from django.db import models
import os

class Honorific(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
class Gender(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class MaritalStatus(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
    

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ACCESS_LEVEL_CHOICES = (
        (3, 'Staff'),
        (2, 'System Admin'),
        (1, 'Super Admin'),
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.ForeignKey(Honorific, on_delete=models.SET_NULL, null=True, blank=True)
    access_level = models.PositiveIntegerField(choices=ACCESS_LEVEL_CHOICES, default=3)
    image = models.ImageField(default='default/user.png', upload_to='Users', null=True, blank=True)
    department = models.ForeignKey('core.Department', on_delete=models.SET_NULL, null=True, related_name='departments')
    division = models.ForeignKey('core.Division', on_delete=models.SET_NULL, null=True, related_name='divisions')
    section = models.ForeignKey('core.Section', on_delete=models.SET_NULL, null=True, related_name='sections')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    career = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    other_roles = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
   
    def __str__(self):
        return f"{self.username} ({self.get_access_level_display()})"
    
    def image_upload_to(self, instance=None, filename=None):
        if instance and filename:
            return os.path.join('Users', self.username, filename)
        return None

    image = models.ImageField(default='default/user.png', upload_to=image_upload_to) 
