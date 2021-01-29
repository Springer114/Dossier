from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('profile', views.profile),
    path('logout', views.logout),
    path('edit_profile/<int:user_id>', views.edit_profile),
    path('update_profile/<int:personal_id>', views.update_profile),
    path('stories', views.stories),
    path('stories/create', views.create_story),
    path('stories/delete/<int:story_id>', views.delete_story)
]