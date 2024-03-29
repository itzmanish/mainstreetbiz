from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .models import Article
from mainstreetbiz.views import static_query
from setting.models import MetaTags


def home(request):
    object_list = Article.objects.all().order_by('-created_At')
    meta = MetaTags.objects.filter(page_name='blog').first()
    paginator = Paginator(object_list, 6)

    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {'articles': articles, 'meta': meta}
    context.update(static_query())
    return render(request, 'blog/blog.html', context)


def details(request, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    context.update(static_query())
    return render(request, 'blog/single_post.html', context)
