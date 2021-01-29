from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('profile', views.profile),
    path('logout', views.logout),
    path('stories', views.stories)
]