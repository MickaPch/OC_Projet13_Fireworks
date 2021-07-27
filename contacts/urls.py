"""Accounts urls"""
from django.urls import path, include
from contacts import views


urlpatterns = [
    path('', views.ContactsHomeView.as_view(), name="contacts_home"),
    path('add_company', views.ContactsAddCompanyFormView.as_view(), name="add_company"),
    path('add_contact_member', views.ContactsAddContactMemberFormView.as_view(), name="add_contact_member"),
    path('add_mission', views.ContactsAddMissionFormView.as_view(), name="add_mission"),
    path('delete_mission', views.ContactsDeleteMissionFormView.as_view(), name="delete_mission"),
]
