from django.urls import path
from App_Login import views

urlpatterns = [
    path('', views.sign_up_view, name='SignUpView'),
    path('profile/', views.profile_view, name='ProfileView'),
    path('edit/', views.edit_profile_view, name='EditProfileView'),
    path('login/', views.log_in_view, name='LogInView'),
    path('logout/', views.log_out_view, name='LogOutView'),
]