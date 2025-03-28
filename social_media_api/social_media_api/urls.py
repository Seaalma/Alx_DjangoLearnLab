from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/auth/', include('accounts.urls')),
    path('api/', include('posts.urls')),
    path('posts/', include('posts.urls')),
    path('notifications/', include('notifications.urls')),
]
