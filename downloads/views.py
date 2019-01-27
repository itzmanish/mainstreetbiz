from django.shortcuts import render
from .models import Document
from mainstreetbiz.views import static_query
from setting.models import MetaTags


def documents(request):
    docs = Document.objects.all()
    meta = MetaTags.objects.filter(page_name='download').first()
    context = {'docs': docs, 'meta': meta}
    context.update(static_query())
    return render(request, 'downloads/downloads.html', context)
