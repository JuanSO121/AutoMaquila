from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def add(value, arg):
    """Concatenates value and arg"""
    return str(value) + str(arg)