from django import template
from contacts.forms import CompanyAddForm

register = template.Library()


@register.inclusion_tag('contacts/form_add_company.html', takes_context=True)
def add_company(context, user):
    company_form = CompanyAddForm()
    
    return {
        'company_form': company_form,
        'user': user
    }
