from distutils.command.upload import upload
from django.db import models
# Importing Django extension user model
from django.contrib.auth.models import User

# Create your models here.

# Creatning child class from Model


class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    # OneToOne relation between this class and User. it does not inherit from it.
    # Due to the db good practices
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    # Allows user to provide a portofolio url
    portfolio_site = models.URLField(blank=True)
    # Allows user to upload the profile picture.
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # Just to print out the user profile info.
    def __str__(self):
        return self.user.username
