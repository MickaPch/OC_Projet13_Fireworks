"""Appliances urls"""
from django.urls import path, include
from appliances import views


urlpatterns = [
    path('', views.AppliancesHomeView.as_view(), name="appliances_home"),
    path('add_task', views.AddTaskFormView.as_view(), name="add_task"),
    path('add_task_input/<int:appliance_pk>', views.add_task_input, name="add_task_input"),
    path('check_task', views.check_task, name="check_task"),
    path('edit_task_description', views.edit_task_description, name="edit_task_description"),
    path('delete_task/<int:task_pk>', views.delete_task, name="delete_task"),
    path('edit_appliance', views.EditApplianceFormView.as_view(), name="edit_appliance"),
    path('edit_appliance_status', views.EditApplianceStatusFormView.as_view(), name="edit_appliance_status"),
    path('notation_chart/<int:appliance_pk>', views.get_notations_chart, name='chart_notations'),
    # path('add_company', views.ContactsAddCompanyFormView.as_view(), name="add_company"),
    # path('delete_company', views.ContactsDeleteCompanyFormView.as_view(), name="delete_company"),
    # path('add_contact', views.ContactsAddContactFormView.as_view(), name="add_contact"),
    # path('edit_contact', views.ContactsEditContactFormView.as_view(), name="edit_contact"),
    # path('delete_contact', views.ContactsDeleteContactFormView.as_view(), name="delete_contact"),
    # path('add_mission', views.ContactsAddMissionFormView.as_view(), name="add_mission"),
    # path('delete_mission', views.ContactsDeleteMissionFormView.as_view(), name="delete_mission"),
]
