from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.show_list, name='show_list'),
    path('<int:post_id>', views.show_post, name='show_post'),
]
