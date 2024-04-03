from django.db import models
# importing User model from Django admin
from django.contrib.auth.models import User

from .utils import user_directory_path

# Create your models here.
class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.address_1} - {self.city}'
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path ,null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    # location = models.OneToOneField('users.Location', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'