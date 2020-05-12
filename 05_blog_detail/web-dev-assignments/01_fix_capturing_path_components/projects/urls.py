from django.urls import path
from . import views


app_name = 'projects'

urlpatterns = [
    path('', views.index, name='projects'),
    path('/?', views.detail, name='project_detail'),
]