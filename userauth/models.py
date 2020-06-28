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

# **********************************************************
# Create User Processing
# *********************************************************


class MyUserManager(BaseUserManager):

    def create_user(self, phone_number, name, password=None):

        user_obj = self.model(
            phone_number=phone_number,
            name=name
        )

        user_obj.set_password(password)
        user_obj.is_admin = False
        user_obj.is_active = True
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, phone_number, name, password=None):

        user_obj = self.create_user(
            phone_number=phone_number,
            name=name,
            password=password,
        )
        user_obj.is_admin = True
        user_obj.save(using=self._db)
        return user_obj


# code for user model

class User(AbstractBaseUser):

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="phone number is not valid")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    name = models.CharField(max_length=50, unique=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# To create a token as soon as user register

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# **********************************************************
# mail and phone validation model and processing
# *********************************************************

class Varification(models.Model):
    phone_number = models.OneToOneField(
        User, to_field='phone_number', on_delete=models.CASCADE)
    email_varification = models.CharField(max_length=20, null=True)
    phone_varification = models.CharField(max_length=20, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


class PhoneOtp(models.Model):
    phone_number = models.OneToOneField(
        User, to_field='phone_number', on_delete=models.CASCADE)
    phone_otp = models.IntegerField()
    counter = models.IntegerField()

    def __str__(self):
        return self.__all__

