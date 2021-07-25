"""Accounts urls"""
from django.urls import path, include
from contacts import views


urlpatterns = [
    path('', views.ContactsHomeView.as_view(), name="contacts_home"),
    path('add_company', views.ContactsAddCompanyFormView.as_view(), name="add_company"),
]
