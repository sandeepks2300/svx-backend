from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title


from django.contrib.auth.models import User


class Post(models.Model):
    caption = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} - {self.caption[:30]}"


# from django.db import models
#
#
# class Post(models.Model):
#     caption = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)


class Media(models.Model):
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/')
    is_video = models.BooleanField(default=False)

    def __str__(self):
        return f"Media for Post {self.post.id}"
