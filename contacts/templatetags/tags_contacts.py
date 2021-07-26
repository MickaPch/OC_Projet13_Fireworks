from django import template
from contacts.forms import CompanyAddForm, ContactMemberAddForm

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
