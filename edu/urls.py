# Create your views here.
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from .views import *


urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'get'})),
    path('<name>', LessonViewSet.as_view({'get': 'get_lesson'})),
]
