from django import template
from appliances.forms import AddTaskForm, EditApplianceForm, EditApplianceStatusForm


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

@register.inclusion_tag('appliances/form_appliance_status.html', takes_context=True)
def form_appliance_status(context, appliance):
    data = {
        'appliance_pk': appliance.pk,
        'status': appliance.status
    }
    form_appliance_status = EditApplianceStatusForm(
        auto_id=False,
        data=data
    )
    
    return {
        'form_appliance_status': form_appliance_status,
        'appliance': appliance
    }

@register.inclusion_tag('appliances/modal_appliance.html', takes_context=True)
def modal_appliance(context, appliance):

    return {
        'appliance': appliance
    }


@register.inclusion_tag('appliances/card_skill.html', takes_context=True)
def card_skill(context, skill):

    return {
        'skill': skill
    }


@register.inclusion_tag('appliances/appliance_bg.html', takes_context=True)
def appliance_bg(context, appliance):

    if appliance.status == 0:
        appliance_background = 'bg-dark text-white'
    elif appliance.status == 10:
        appliance_background = 'bg-warning'
    elif appliance.status == 20:
        appliance_background = 'bg-primary text-white'
    elif appliance.status == 30:
        appliance_background = 'bg-success'
    elif appliance.status == 40:
        appliance_background = 'bg-secondary text-white'
    elif appliance.status == 50:
        appliance_background = 'bg-danger text-white'
    else:
        appliance_background = ''

    return {
        'appliance': appliance,
        'appliance_background': appliance_background
    }


@register.inclusion_tag('appliances/appliance_title.html', takes_context=True)
def appliance_title(context, appliance):

    if appliance.status == 0:
        appliance_status_icon = 'far fa-lightbulb'
    elif appliance.status == 10:
        appliance_status_icon = 'fas fa-tasks'
    elif appliance.status == 20:
        appliance_status_icon = 'far fa-clock'
    elif appliance.status == 30:
        appliance_status_icon = 'fas fa-check'
    elif appliance.status == 40:
        appliance_status_icon = 'fas fa-ban'
    elif appliance.status == 50:
        appliance_status_icon = 'fas fa-window-close'
    else:
        appliance_status_icon = ''

    return {
        'appliance': appliance,
        'appliance_status_icon': appliance_status_icon
    }


@register.inclusion_tag('appliances/chart_appliance.html', takes_context=True)
def chart_appliance(context, appliance):

    # appliance_datas = appliance.get_notations_list()

    return {
        'appliance': appliance
    }

@register.inclusion_tag('appliances/timeline_appliance.html', takes_context=True)
def timeline_appliance(context, appliance):

    return {
        'appliance': appliance
    }


@register.inclusion_tag('appliances/badge_event.html', takes_context=True)
def badge_event(context, event):

    if event.type == "MEE":
        event_badge = 'badge badge-event-xl badge-primary fas fa-calendar-alt'
    elif event.type == "PHC":
        event_badge = 'badge badge-event-xl badge-secondary fas fa-phone'
    elif event.type == "APY":
        event_badge = 'badge badge-event-xl badge-primary fas fa-calendar-plus'
    elif event.type == "OFR":
        event_badge = 'badge badge-event-xl badge-success fa fa-check'
    elif event.type == "TES":
        event_badge = 'badge badge-event-xl badge-info fas fa-pencil-alt'
    else:
        event_badge = 'badge badge-event-xl badge-primary'

    return {
        'event': event,
        'event_badge': event_badge
    }

@register.inclusion_tag('appliances/form_add_task.html', takes_context=True)
def form_add_task(context, user, appliance=None):

    data = {
        'user_pk': user.pk
    }
    if appliance is not None:
        data['appliance_pk'] = appliance.pk

    form_add_task = AddTaskForm(
        auto_id=False,
        data=data
    )
    
    return {
        'form_add_task': form_add_task,
        'user': user
    }
