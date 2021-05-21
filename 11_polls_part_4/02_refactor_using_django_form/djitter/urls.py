from django.contrib import admin
from django.urls import path, include
from profile.views import frontpage


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('profile/', include('profile.urls')),
    path('feed/', include('feed.urls')),
    path('admin/', admin.site.urls),
]
