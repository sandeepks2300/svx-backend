from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from . import models


class HomePageView(TemplateView):
    template_name = 'home.html'


def video_list(request):
    videos = models.Video.objects.all()
    return render(request, 'video-list.html', {'videos': videos})


def post_list(request):
    posts = models.Post.objects.prefetch_related('media').order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})


def upload_post(request):
    if request.method == 'POST':
        caption = request.POST.get('caption', '')
        files = request.FILES.getlist('media_files')

        if files:
            post = models.Post.objects.create(caption=caption)
            for file in files:
                is_video = file.content_type.startswith('video/')
                models.Media.objects.create(post=post, file=file, is_video=is_video)
            return redirect('post_list')  # Update with your post list URL name

    return render(request, 'upload-post.html')
