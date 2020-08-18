from django import template
from articles.models import ImageModel, TextModel

register = template.Library()


@register.filter
def check_image(value):
    return type(value) == ImageModel


@register.filter
def check_text(value):
    return type(value) == TextModel


@register.filter
def capitalize_all(value):
    return value.upper()
