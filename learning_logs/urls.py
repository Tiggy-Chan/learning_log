"""Defines templates of URL for learning_logs"""
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Main site
    path('', views.index, name='index'),
    # Displaying all topics
    path('topics/', views.topics, name='topics'),
    # Page of specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new entries
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
