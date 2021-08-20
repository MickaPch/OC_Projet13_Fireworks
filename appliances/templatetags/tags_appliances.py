from django import template
from appliances.forms import AddTaskForm, EditApplianceForm, EditApplianceStatusForm, EditTaskForm, CheckTaskForm


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

    event_badge = event.get_badge()

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

@register.inclusion_tag('appliances/card_task.html', takes_context=True)
def card_task(context, appliance):

    return {
        'appliance': appliance
    }

@register.inclusion_tag('appliances/checkbox_task.html', takes_context=True)
def checkbox_task(context, task):

    data_checkbox = {
        'task_pk': task.pk,
        'done': task.done
    }
    data_description = {
        'task_pk': task.pk,
        'description': task.description
    }
    data_delete = {
        'task_pk': task.pk
    }

    form_check_task = CheckTaskForm(
        auto_id=f'form_check_task_%s_{str(task.pk)}',
        data=data_checkbox
    )
    form_edit_description = EditTaskForm(
        auto_id=f'form_description_task_%s_{str(task.pk)}',
        data=data_description
    )

    return {
        'form_check_task': form_check_task,
        'form_edit_description': form_edit_description,
        'task': task
    }

@register.inclusion_tag('appliances/input_new_task.html', takes_context=True)
def input_new_task (context, appliance):

    data_checkbox = {
        'appliance_pk': appliance.pk,
        'user_pk': appliance.user.pk
    }

    form_add_task = AddTaskForm(
        auto_id=f'form_input_task_%s_{str(appliance.pk)}',
        data=data_checkbox
    )

    return {
        'form_add_task': form_add_task,
        'appliance': appliance
    }
