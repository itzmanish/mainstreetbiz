from django import template

from feeds.models import FeedPost

register = template.Library()


@register.filter
def feeds_comments(number_of_results):
    return FeedPost.objects.order_by('-date')[:number_of_results]
