from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter(name='groups')
def groups(user, group_name):
    return Group.objects.filter(name=group_name, user=user).exists()
