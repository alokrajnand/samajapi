from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from .views import *


urlpatterns = [
    path('', SubscriptionViewSet.as_view({'get': 'get'})),
    path('<name>', SubscriptionViewSet.as_view({'get': 'get_subscription'})),
    path('sub/', SubscriptionViewSet.as_view({'post': 'post_subscription'})),
]
