from django.db import models

# Create your models here.

# **********************************************************
# Profile Model
# *********************************************************


from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.validators import RegexValidator
# write the code of user manager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import datetime
from userauth.models import *

# **********************************************************
# User Profile model and processing
# *********************************************************


class Profile(models.Model):
    phone_number = models.OneToOneField(
        User, to_field='phone_number', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email_address = models.EmailField(max_length=200, unique=False),
    user_designation = models.CharField(max_length=200, null=True)
    user_tag_line = models.CharField(max_length=200, null=True)
    user_tag_line_desc = models.CharField(max_length=300, null=True)
    user_date_of_birth = models.DateField(null=True)
    user_profile_pic_link = models.CharField(max_length=200, null=True)
    user_banner_pic_link = models.CharField(max_length=200, null=True)
    user_address_landmark = models.CharField(max_length=200, null=True)
    user_city = models.CharField(max_length=60, null=True)
    user_district = models.CharField(max_length=60, null=True)
    user_state = models.CharField(max_length=60, null=True)
    user_country = models.CharField(max_length=60, null=True)
    user_pincode = models.IntegerField(null=True)
    user_twitter_link = models.CharField(max_length=200, null=True)
    user_git_hub_link = models.CharField(max_length=200, null=True)
    user_linkdin_link = models.CharField(max_length=200, null=True)
    user_faebook_link = models.CharField(max_length=200, null=True)
    user_instagram_link = models.CharField(max_length=200, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
