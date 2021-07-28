from django import template
from contacts.forms import CompanyAddForm, ContactMemberAddForm, MissionAddForm, MissionDeleteForm

register = template.Library()


@register.inclusion_tag('contacts/form_add_company.html', takes_context=True)
def form_add_company(context, user):
    company_form = CompanyAddForm()
    
    return {
        'company_form': company_form,
        'user': user
    }

@register.inclusion_tag('contacts/form_add_contact_member.html', takes_context=True)
def form_add_contact_member(context, company):
    contact_member_form = ContactMemberAddForm()
    
    return {
        'contact_member_form': contact_member_form,
        'company': company
    }

@register.inclusion_tag('contacts/form_add_mission.html', takes_context=True)
def form_add_mission(context, company):
    add_mission_form = MissionAddForm()
    
    return {
        'add_mission_form': add_mission_form,
        'company': company
    }

@register.inclusion_tag('contacts/form_delete_mission.html', takes_context=True)
def form_delete_mission(context, mission_title, company):
    data = {
        'title': mission_title,
        'company': company
    }
    delete_mission_form = MissionDeleteForm(data=data)
    
    return {
        'delete_mission_form': delete_mission_form,
        'mission_title': mission_title
    }
