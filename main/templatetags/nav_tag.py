from django import template
from ..models import Nav


register = template.Library()


@register.simple_tag()
def get_nav():
    return Nav.objects.all()