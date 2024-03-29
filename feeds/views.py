from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from .models import FeedPost
from mainstreetbiz.views import static_query
from setting.models import MetaTags


def feeds(request):
    object_list = FeedPost.objects.order_by('-date')
    meta = MetaTags.objects.filter(page_name='news').first()
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    feeds = paginator.get_page(page)
    context = {'news': feeds, 'meta': meta}
    context.update(static_query())
    return render(request, 'feeds/feeds.html', context)
