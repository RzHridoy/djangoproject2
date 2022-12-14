from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    post_image = models.ImageField(upload_to='post_images')
    caption = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-upload_date']


class LikeModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='liked_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')
    date_created = models.DateTimeField(auto_now_add=True)
