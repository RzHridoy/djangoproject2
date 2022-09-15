from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from App_Login import forms, models
from App_Post.forms import PostModelForm

# Create your views here.


def sign_up_view(request):
    form = forms.CreateNewUserForm()

    registered = False
    if request.method == 'POST':
        form = forms.CreateNewUserForm(data=request.POST)

        if form.is_valid():
            form.save()
            registered = True
            return HttpResponseRedirect(reverse('LogInView'))
    return render(request, 'App_Login/sign_up.html', context={'form': form})


def log_in_view(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('ProfileView'))
    return render(request, 'App_Login/log_in.html', context={'form': form})


@login_required()
def log_out_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('LogInView'))


@login_required()
def profile_view(request):
    form = PostModelForm()

    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('HomeView'))
    return render(request, 'App_Login/profile.html', context={'form': form})


@login_required()
def edit_profile_view(request):
    current_user = models.UserProfileModel.objects.get(user=request.user)
    form = forms.EditUserProfileForm(instance=current_user)

    if request.method == 'POST':
        form = forms.EditUserProfileForm(request.POST, request.FILES, instance=current_user)

        if form.is_valid():
            form.save()
            form = forms.EditUserProfileForm(instance=current_user)
            return HttpResponseRedirect(reverse('ProfileView'))

    return render(request, 'App_Login/edit_profile.html', context={'form': form})


