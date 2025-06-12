from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from svx_main.models import Post, Media
from .serializers import PostSerializer

# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#
#     if not username or not password:
#         return Response({'error': 'Username and password required.'}, status=status.HTTP_400_BAD_REQUEST)
#
#     user = authenticate(request, username=username, password=password)
#
#     if user is not None:
#         # Optionally create a token here if using token auth
#         return Response({'message': 'Login successful!'}, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)

import json
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        except Exception as e:
            return JsonResponse({'message': 'Invalid data'}, status=400)

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        return JsonResponse({'message': 'Invalid credentials'}, status=401)
    return JsonResponse({'message': 'Method not allowed'}, status=405)


# @api_view(['POST'])
# @parser_classes([MultiPartParser, FormParser])
# def upload_post_api(request):
#     caption = request.data.get('caption', '')
#     files = request.FILES.getlist('images')  # match the frontend FormData key
#
#     if not files:
#         return Response({'error': 'No media files uploaded.'}, status=status.HTTP_400_BAD_REQUEST)
#
#     post = Post.objects.create(caption=caption)
#
#     for file in files:
#         is_video = file.content_type.startswith('video/')
#         Media.objects.create(post=post, file=file, is_video=is_video)
#
#     return Response({'message': 'Post uploaded successfully.'}, status=status.HTTP_201_CREATED)
@csrf_exempt
# @permission_classes([IsAuthenticated])
@api_view(['POST'])
def upload_post_api(request):
    caption = request.POST.get('caption', '')
    files = request.FILES.getlist('media_files')  # Support multiple file uploads
    User = get_user_model()
    user = User.objects.get(username=request.GET.get('user'))
    if not files:
        return Response({'error': 'No media files provided'}, status=400)

    # Create post associated with the current authenticated user
    post = Post.objects.create(caption=caption, user=user)

    for file in files:
        is_video = file.content_type.startswith('video/')
        Media.objects.create(post=post, file=file, is_video=is_video)

    return Response({'message': 'Post uploaded successfully'}, status=201)


@api_view(['GET'])
# def post_list_api(request):
#     print("HE")
#     posts = Post.objects.prefetch_related('media').order_by('-created_at')
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)
def post_list_api(request):
    user = request.GET.get('user')
    exclude = request.GET.get('exclude')
    posts = Post.objects.all()

    if user:
        posts = posts.filter(user__username=user)
    elif exclude:
        posts = posts.exclude(user__username=exclude)

    serializer = PostSerializer(posts.order_by('-created_at'), many=True)
    return Response(serializer.data)