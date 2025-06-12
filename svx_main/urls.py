from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('my-videos/', views.video_list, name='my_videos'),
    path('upload/', views.upload_post, name='upload_post'),
]
