# Generated by Django 3.0.3 on 2020-06-28 08:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
