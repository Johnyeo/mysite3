from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<int:character_id>/', views.profile, name='profile'),
    path('init_db/<int:db_id>/', views.initializeDatabase, name='init_db'),
    # /game/2/profile
]