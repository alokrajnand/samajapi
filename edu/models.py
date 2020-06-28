from django.db import models
from datetime import datetime
# Create your models here.

# **********************************************************
# Course  Model
# *********************************************************


class Course(models.Model):
    course_id = models.CharField(max_length=50, unique=True, null=False)
    course_name = models.CharField(max_length=50, unique=True, null=False)
    course_category = models.CharField(max_length=50, unique=True, null=False)
    course_owner = models.CharField(max_length=50, null=True)
    course_short_desc = models.CharField(max_length=100, null=True)
    course_desc = models.CharField(max_length=5000, null=True)
    course_image_path = models.CharField(max_length=200, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__


class Lesson(models.Model):
    lesson_id = models.CharField(max_length=50, unique=True, null=False)
    course_id = models.ForeignKey(
        Course, to_field='course_id', on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=50, unique=True, null=False)
    lesson_owner = models.CharField(max_length=50, null=True)
    lesson_short_desc = models.CharField(max_length=100, null=True)
    lesson_desc = models.CharField(max_length=5000, null=True)
    lesson_image_path = models.CharField(max_length=200, null=True)
    lesson_video_path = models.CharField(max_length=200, null=True)
    created_dt = models.DateTimeField(default=datetime.now, null=True)
    updated_dt = models.DateTimeField(default=datetime.now, null=True)

    def __str__(self):
        return self.__all__
