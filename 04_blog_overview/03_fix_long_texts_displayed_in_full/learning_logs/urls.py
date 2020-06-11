"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views


app_name = 'learning_logs'

urlpatterns = [
    # homepage
    path('', views.index, name='index'),
    # topics
    path('topics/', views.topics, name='topics'),
    # entries
    path('topics/<int:pk>/', views.entry, name='entry'),
]