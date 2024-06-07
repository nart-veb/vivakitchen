from django import template
from ..models import ShowNav


register = template.Library()


@register.simple_tag()
def get_shownav():
    return ShowNav.objects.all()