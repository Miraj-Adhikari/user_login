from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active_class(context, url_name):
    return '' if context['request'].resolver_match.url_name == url_name else 'collapsed'