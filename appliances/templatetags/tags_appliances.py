from django import template
from appliances.forms import EditApplianceForm


register = template.Library()


@register.inclusion_tag('appliances/form_edit_appliance.html', takes_context=True)
def form_edit_appliance(context, appliance):
    data = {
        'appliance_pk': appliance.pk,
        'status': appliance.status,
        'estimated_salary': appliance.estimated_salary,
        'proposed_salary': appliance.proposed_salary,
        'environment_notation': appliance.environment_notation,
        'environment_details': appliance.environment_details,
        'values_notation': appliance.values_notation,
        'values_details': appliance.values_details,
        'evolution_notation': appliance.evolution_notation,
        'evolution_details': appliance.evolution_details,
        'knowledge_notation': appliance.knowledge_notation,
        'knowledge_details': appliance.knowledge_details,
        'management_notation': appliance.management_notation,
        'management_details': appliance.management_details,
        'advantages_notation': appliance.advantages_notation,
        'advantages_details': appliance.advantages_details,
        'notoriety_notation': appliance.notoriety_notation,
        'notoriety_details': appliance.notoriety_details,
        'office_notation': appliance.office_notation,
        'office_details': appliance.office_details
    }
    edit_appliance_form = EditApplianceForm(
        auto_id=False,
        data=data
    )
    
    return {
        'edit_appliance_form': edit_appliance_form,
        'appliance': appliance
    }

@register.inclusion_tag('appliances/appliance_bg.html', takes_context=True)
def appliance_bg(context, appliance):

    if appliance.status == 10:
        appliance_background = 'bg-light'
    elif appliance.status == 20:
        appliance_background = 'bg-info'
    elif appliance.status == 30:
        appliance_background = 'bg-dark text-white'
    elif appliance.status == 40:
        appliance_background = 'bg-warning'
    elif appliance.status == 50:
        appliance_background = 'bg-primary text-white'
    elif appliance.status == 60:
        appliance_background = 'bg-success'
    elif appliance.status == 70:
        appliance_background = 'bg-secondary text-white'
    elif appliance.status == 80:
        appliance_background = 'bg-danger text-white'
    else:
        appliance_background = ''

    return {
        'appliance': appliance,
        'appliance_background': appliance_background
    }


@register.inclusion_tag('appliances/chart_appliance.html', takes_context=True)
def chart_appliance(context, appliance):

    # appliance_datas = appliance.get_notations_list()

    return {
        'appliance': appliance
    }
