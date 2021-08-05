from django import template
from appliances.forms import EditApplianceForm


register = template.Library()


@register.inclusion_tag('appliances/form_edit_appliance.html', takes_context=True)
def form_edit_appliance(context, appliance_to_edit):
    data = {
        'appliance_pk': appliance_to_edit.pk,
        'estimated_salary': appliance_to_edit.estimated_salary,
        'proposed_salary': appliance_to_edit.proposed_salary,
        'environment_notation': appliance_to_edit.environment_notation,
        'environment_details': appliance_to_edit.environment_details,
        'values_notation': appliance_to_edit.values_notation,
        'values_details': appliance_to_edit.values_details,
        'evolution_notation': appliance_to_edit.evolution_notation,
        'evolution_details': appliance_to_edit.evolution_details,
        'knowledge_notation': appliance_to_edit.knowledge_notation,
        'knowledge_details': appliance_to_edit.knowledge_details,
        'management_notation': appliance_to_edit.management_notation,
        'management_details': appliance_to_edit.management_details,
        'advantages_notation': appliance_to_edit.advantages_notation,
        'advantages_details': appliance_to_edit.advantages_details,
        'notoriety_notation': appliance_to_edit.notoriety_notation,
        'notoriety_details': appliance_to_edit.notoriety_details,
        'office_notation': appliance_to_edit.office_notation,
        'office_details': appliance_to_edit.office_details
    }
    edit_appliance_form = EditApplianceForm(data=data)
    
    return {
        'edit_appliance_form': edit_appliance_form,
        'appliance_to_edit': appliance_to_edit
    }
