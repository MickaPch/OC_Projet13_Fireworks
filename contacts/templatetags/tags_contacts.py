from django import template
from django.http import request
from contacts.forms import CompanyAddForm, EditCompanyForm, AddContactForm, DeleteContactForm, EditContactForm, CompanyDeleteForm

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

@register.inclusion_tag('contacts/form_edit_company.html', takes_context=True)
def form_edit_company(context, company_to_edit):
    data = {
        'company_pk': company_to_edit.pk,
        'name': company_to_edit.name,
        'address1': company_to_edit.address1,
        'address2': company_to_edit.address2,
        'zipcode': company_to_edit.zipcode,
        'city': company_to_edit.city
    }
    edit_company_form = EditCompanyForm(data=data)
    
    return {
        'edit_company_form': edit_company_form,
        'company_to_edit': company_to_edit
    }


@register.inclusion_tag('contacts/form_delete_company.html', takes_context=True)
def form_delete_company(context, company, user):
    data = {
        'company_pk': company.pk,
        'user': user
    }
    delete_company_form = CompanyDeleteForm(data=data)
    
    return {
        'delete_company_form': delete_company_form,
        'user': user
    }


@register.inclusion_tag('contacts/form_add_contact.html', takes_context=True)
def form_add_contact(context, user, company=None):

    data = {}
    if company is not None:
        data['company'] = company.pk

    add_contact_form = AddContactForm(
        auto_id=False,
        data=data
    )
    
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

# @register.inclusion_tag('contacts/form_add_mission.html', takes_context=True)
# def form_add_mission(context, user, company=None):

#     data = {}
#     if company is not None:
#         data['company'] = company.pk

#     add_mission_form = MissionAddForm(
#         auto_id=False,
#         data=data
#     )
    
#     return {
#         'add_mission_form': add_mission_form,
#         'user': user
#     }

# @register.inclusion_tag('contacts/form_delete_mission.html', takes_context=True)
# def form_delete_mission(context, mission_title, company, user):
#     data = {
#         'title': mission_title,
#         'company': company,
#         'user': user
#     }
#     delete_mission_form = MissionDeleteForm(data=data)
    
#     return {
#         'delete_mission_form': delete_mission_form,
#         'mission_title': mission_title,
#         'user': user
#     }

@register.inclusion_tag('contacts/add_btn.html', takes_context=True)
def add_to_company_btn(context, company, user):
    data = {
        'company': company,
        'user': user
    }
    # delete_mission_form = MissionDeleteForm(data=data)
    
    return {
        # 'delete_mission_form': delete_mission_form,
        'company': company,
        'user': user
    }

@register.inclusion_tag('contacts/company_title.html', takes_context=True)
def company_title(context, company, user):

    if company.type == 'ESN':
        company_icon = 'fas fa-desktop'
    elif company.type == 'SOFT':
        company_icon = 'fas fa-laptop-code'
    elif company.type == 'ENG':
        company_icon = 'fas fa-tools'
    elif company.type == 'IND':
        company_icon = 'fas fa-industry'
    elif company.type == 'WEB':
        company_icon = 'fas fa-wifi'
    else:
        company_icon = 'fas fa-building'

    return {
        'company': company,
        'company_icon': company_icon,
        'user': user
    }


@register.inclusion_tag('contacts/activity_icons.html', takes_context=True)
def activity_icons(context, company):

    business_icons_list = list()
    for business in company.business.all():
        icon = business.name + '///' + business.fa_icon
        business_icons_list.append(icon)
    
    business_icons_list = "---".join(business_icons_list)

    return {
        'company': company,
        'business_icons_list': business_icons_list
    }

