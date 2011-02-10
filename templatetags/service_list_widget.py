from django import template

register = template.Library()

@register.inclusion_tag('service_list.html')
def service_list_widget(services,*args):
    return {'services': services}
