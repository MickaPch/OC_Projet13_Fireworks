from django import template
from django.http import request
from contacts.forms import CompanyAddForm, AddContactForm, DeleteContactForm, EditContactForm, MissionAddForm, MissionDeleteForm, CompanyDeleteForm

import json

register = template.Library()


@register.inclusion_tag('contacts/form_add_company.html', takes_context=True)
def form_add_company(context, user):

    company_form = CompanyAddForm()

    context_add_company = {
        'company_form': company_form,
        'user': user
    }
    
    return context_add_company


@register.inclusion_tag('contacts/form_delete_company.html', takes_context=True)
def form_delete_company(context, company, user):
    data = {
        'name': company,
        'user': user
    }
    delete_company_form = CompanyDeleteForm(data=data)
    
    return {
        'delete_company_form': delete_company_form,
        'user': user
    }


@register.inclusion_tag('contacts/form_add_contact.html', takes_context=True)
def form_add_contact(context, user):
    add_contact_form = AddContactForm()
    
    return {
        'add_contact_form': add_contact_form,
        'user': user
    }

@register.inclusion_tag('contacts/form_edit_contact.html', takes_context=True)
def form_edit_contact(context, contact_to_edit):
    data = {
        'contact_pk': contact_to_edit.pk,
        'first_name': contact_to_edit.first_name,
        'last_name': contact_to_edit.last_name,
        'phone_number': contact_to_edit.phone_number,
        'email': contact_to_edit.email,
        'company': contact_to_edit.company.pk
    }
    edit_contact_form = EditContactForm(data=data)
    
    return {
        'edit_contact_form': edit_contact_form,
        'contact_to_edit': contact_to_edit
    }

@register.inclusion_tag('contacts/form_delete_contact.html', takes_context=True)
def form_delete_contact(context, contact_pk, user):
    data = {
        'contact_pk': contact_pk,
        'user': user
    }
    delete_contact_form = DeleteContactForm(data=data)
    
    return {
        'delete_contact_form': delete_contact_form,
        'user': user
    }

@register.inclusion_tag('contacts/form_add_mission.html', takes_context=True)
def form_add_mission(context, user):
    add_mission_form = MissionAddForm()
    
    return {
        'add_mission_form': add_mission_form,
        'user': user
    }

@register.inclusion_tag('contacts/form_delete_mission.html', takes_context=True)
def form_delete_mission(context, mission_title, company, user):
    data = {
        'title': mission_title,
        'company': company,
        'user': user
    }
    delete_mission_form = MissionDeleteForm(data=data)
    
    return {
        'delete_mission_form': delete_mission_form,
        'mission_title': mission_title,
        'user': user
    }
