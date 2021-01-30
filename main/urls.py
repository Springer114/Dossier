from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('profile', views.profile),
    path('logout', views.logout),
    path('profile/edit/<int:user_id>', views.edit_profile),
    path('profile/update/<int:user_id>', views.update_profile),
    path('stories', views.stories),
    path('stories/create', views.create_story),
    path('stories/edit/<int:story_id>', views.edit_story),
    path('stories/delete/<int:story_id>', views.delete_story)
]