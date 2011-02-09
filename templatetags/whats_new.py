from django import template
from uwregistry.rss import RSS

register = template.Library()

@register.inclusion_tag('whats_new_widget.html', takes_context=True)
def whats_new_widget(context):
    return {'rss' : RSS()}
