from django.shortcuts import render
from .models import Document
from mainstreetbiz.views import static_query


def documents(request):
    docs = Document.objects.all()
    context = {'docs': docs}
    context.update(static_query())
    return render(request, 'downloads/downloads.html', context)
