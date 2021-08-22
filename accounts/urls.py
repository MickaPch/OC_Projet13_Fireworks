"""Accounts urls"""
from django.urls import path, include
from accounts import views


urlpatterns = [
    path('home/', views.AccountsHomeView.as_view(), name="accounts_home_page"),
    path('profile/', views.AccountsProfileView.as_view(),
         name="accounts_profile_page"),
    path('edit_username', views.edit_username, name="edit_username"),
    path('edit_name', views.edit_name, name="edit_name"),
    path('edit_email', views.edit_email, name="edit_email"),
    path('', include("django.contrib.auth.urls")),
]
