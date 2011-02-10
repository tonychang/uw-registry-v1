from django import template
from uwregistry.tweets import get_tweets

register = template.Library()

@register.inclusion_tag('twitter_widget.html', takes_context=True)
def twitter_widget(context):
    return {'tweets' : get_tweets()}
