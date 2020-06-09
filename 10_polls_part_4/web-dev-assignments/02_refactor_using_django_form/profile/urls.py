from django.urls import path
from profile import views


#app_name = 'profile'

urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/following', views.following, name='following'),
    path('<str:username>/followers', views.followers, name='followers'),
    path('<str:username>/follow', views.follow, name='follow'),
    path('<str:username>/stopfollow', views.stopfollow, name='stopfollow'),
    path('signout/', views.signout, name='signout'),
]