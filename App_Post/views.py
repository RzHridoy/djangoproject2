from django.shortcuts import render

from App_Login.models import UserProfileModel
from App_Post.models import PostModel
from django.contrib.auth.models import User
# Create your views here.


def home_view(request):
    user_list = UserProfileModel.objects.all()
    users_list = User.objects.all()
    user_post_list = PostModel.objects.all()
    return render(request, 'App_Post/home.html', context={
        'user_list': user_list,
        'users_list': users_list,
        'user_post_list': user_post_list
    })
