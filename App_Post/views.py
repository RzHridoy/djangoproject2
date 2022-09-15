from django.shortcuts import render

from App_Login.models import UserProfileModel
from App_Post.models import PostModel

# Create your views here.


def home_view(request):
    user_list = UserProfileModel.objects.all()
    user_post_list = PostModel.objects.all()
    return render(request, 'App_Post/home.html', context={
        'user_list': user_list,
        'user_post_list': user_post_list
    })
