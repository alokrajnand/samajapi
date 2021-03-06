# Generated by Django 3.0.3 on 2020-06-17 14:32

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='phone number is not valid', regex='^\\+?1?\\d{9,15}$')])),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Varification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_varification', models.CharField(max_length=20, null=True)),
                ('phone_varification', models.CharField(max_length=20, null=True)),
                ('created_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('phone_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='phone_number')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('user_designation', models.CharField(max_length=200, null=True)),
                ('user_tag_line', models.CharField(max_length=200, null=True)),
                ('user_tag_line_desc', models.CharField(max_length=300, null=True)),
                ('user_date_of_birth', models.DateField(null=True)),
                ('user_profile_pic_link', models.CharField(max_length=200, null=True)),
                ('user_banner_pic_link', models.CharField(max_length=200, null=True)),
                ('user_address', models.CharField(max_length=200, null=True)),
                ('user_city', models.CharField(max_length=60, null=True)),
                ('user_state', models.CharField(max_length=60, null=True)),
                ('user_country', models.CharField(max_length=60, null=True)),
                ('user_twitter_link', models.CharField(max_length=200, null=True)),
                ('user_git_hub_link', models.CharField(max_length=200, null=True)),
                ('user_linkdin_link', models.CharField(max_length=200, null=True)),
                ('user_faebook_link', models.CharField(max_length=200, null=True)),
                ('user_instagram_link', models.CharField(max_length=200, null=True)),
                ('created_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('phone_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='phone_number')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneOtp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_otp', models.IntegerField()),
                ('counter', models.IntegerField()),
                ('phone_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='phone_number')),
            ],
        ),
    ]
