from django.db import models
from datetime import datetime
# Create your models here.

# **********************************************************
# Course  Model
# *********************************************************


class Product(models.Model):
    procuct_id = models.CharField(max_length=50, unique=True, null=False)
    product_name = models.CharField(max_length=50, unique=True, null=False)
    product_price = models.IntegerField(null=False)
    product_category = models.CharField(max_length=50, unique=True, null=False)
    product_owner = models.CharField(max_length=50, null=True)
    product_short_desc = models.CharField(max_length=100, null=True)
    product_desc = models.CharField(max_length=5000, null=True)
    prodcut_image_pat = models.CharField(max_length=200, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
