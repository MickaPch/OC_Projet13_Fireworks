from django import template
from django.http import request
from contacts.forms import CompanyAddForm, ContactMemberAddForm, MissionAddForm, MissionDeleteForm

register = template.Library()


@register.inclusion_tag('contacts/form_add_company.html', takes_context=True)
def form_add_company(context, user):

    if 'company_form_data' in context.request.session:
        data = context.request.session['company_form_data']
    else:
        data = {}

    company_form = CompanyAddForm(data)
    context_add_company = {
        'company_form': company_form,
        'user': user
    }

    if 'company_form_errors' in context.request.session:
        context_add_company['company_form_errors'] = context.request.session['company_form_errors']
    
    return context_add_company

@register.inclusion_tag('contacts/form_add_contact_member.html', takes_context=True)
def form_add_contact_member(context):
    contact_member_form = ContactMemberAddForm()
    
    return {
        'contact_member_form': contact_member_form
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
