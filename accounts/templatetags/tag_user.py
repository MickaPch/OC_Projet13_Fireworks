from django import template


register = template.Library()


@register.inclusion_tag('accounts/accounts.html', takes_context=True)
def user_homeview(context, user):
    return {'user': user}
