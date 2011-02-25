from django import template
from uwregistry.rss import RSS
from django.conf import settings

register = template.Library()

@register.inclusion_tag('whats_new_widget.html', takes_context=True)
def whats_new_widget(context):
    return {'rss_entries' : RSS().entries()[:5],'blog_url' : settings.BLOG_URL,}
