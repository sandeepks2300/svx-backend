from django.urls import path
from .views import login_view, upload_post_api, post_list_api

urlpatterns = [
    path('login', login_view, name='login'),
    path('upload-post', upload_post_api, name='upload_post_api'),
    path('posts/', post_list_api, name='post_list_api'),
]
