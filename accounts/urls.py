"""Accounts urls"""
from django.urls import path, include
from accounts import views


urlpatterns  = [
    path('home/', views.AccountsHomeView.as_view(), name="accounts_home_page"),
    path('', include("django.contrib.auth.urls")),
]