# Create your views here.
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from .views import *


urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'get'})),

]
