
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('userauth.urls')),
    path('api/product/', include('product.urls')),
    path('api/subscription/', include('subscription.urls')),
    path('api/profile/', include('userprofile.urls')),
    path('api/course/', include('edu.urls')),
]
