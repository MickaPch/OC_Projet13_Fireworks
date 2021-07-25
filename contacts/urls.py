"""Accounts urls"""
from django.urls import path, include
from contacts import views


urlpatterns = [
    path('', views.ContactsHomeView.as_view(), name="contacts_home_page"),
]
