from django.db import models
from datetime import datetime
# Create your models here.

# **********************************************************
# Course  Model
# *********************************************************


class Subscription(models.Model):
    product_id = models.CharField(max_length=50,  null=False)
    product_name = models.CharField(max_length=50,  null=False)
    prodcut_image_pat = models.CharField(max_length=200, null=True)
    product_price = models.IntegerField(null=False)
    subscription_price = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
    subscription_type = models.CharField(max_length=50, null=False)
    subscription_status = models.CharField(max_length=50,  null=False)
    user_id = models.CharField(max_length=50, null=False)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
