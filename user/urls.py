"""User urls"""
from django.urls import path, include
from user import views


urlpatterns  = [
    path('home/', views.UserView.as_view(), name="user_page"),
    path('', include("django.contrib.auth.urls")),
]