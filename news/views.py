from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from mainstreetbiz.views import static_query
from .models import News


def home(request):
    object_list = News.objects.all().order_by('-created_At')
    paginator = Paginator(object_list, 6)

    page = request.GET.get('page')
    news = paginator.get_page(page)
    context = {'news': news}
    context.update(static_query())
    return render(request, 'news/home.html', context)


def details(request, slug):
    news = News.objects.get(slug=slug)
    context = {'news': news}
    context.update(static_query())
    return render(request, 'news/single_news.html', context)
