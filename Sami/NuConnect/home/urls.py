"""
Home URLs
"""
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('announcements', views.announcements, name='announcements'),
    path('resources', views.resources, name='resources'),
    path('attendance', views.attendance, name='attendance'),
    path('grades', views.grades, name='grades'),
    path('assignments', views.assignments, name='assignments'),
    path('profile', views.profile, name='profile')
]
