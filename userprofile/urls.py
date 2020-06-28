from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from .views import *

urlpatterns = [
    path('<name>', ProfileViewSet.as_view({'get': 'get_profile'})),
    path('insert/', ProfileViewSet.as_view({'post': 'post_profile'})),
    path('update/<name>',
         ProfileViewSet.as_view({'put': 'put_profile'}))
]
