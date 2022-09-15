from django.urls import path
from App_Post import views


urlpatterns = [
    path('', views.home_view, name='HomeView'),
]
