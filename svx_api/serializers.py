from rest_framework import serializers
from svx_main.models import Post, Media
from django.contrib.auth import get_user_model

User = get_user_model()


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'file', 'is_video']


# class PostSerializer(serializers.ModelSerializer):
#     media = MediaSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Post
#         fields = ['id', 'caption', 'created_at', 'media']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PostSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)  # 👈 Add this

    class Meta:
        model = Post
        fields = ['id', 'caption', 'created_at', 'media', 'user']
