from django.shortcuts import render, HttpResponse
# Create your views here.
from .models import FeedPost
# from .feeds import handle
from mainstreetbiz.views import static_query


def feeds(request):
    feeds = FeedPost.objects.order_by('-date')
    context = {'rss_feeds': feeds}
    context.update(static_query())
    return render(request, 'feeds/feeds.html', context)
