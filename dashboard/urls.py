"""Accounts urls"""
from django.urls import path, include
from dashboard import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
]
