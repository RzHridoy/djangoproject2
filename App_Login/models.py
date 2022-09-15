from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    full_name = models.CharField(max_length=50, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    description = models.TextField(blank=True)
    dob = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)


class FollowModel(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created_follow_date = models.DateTimeField(auto_now_add=True)