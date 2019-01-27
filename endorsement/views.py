from django.shortcuts import render
from mainstreetbiz.views import static_query
from .models import Clients
from setting.models import MetaTags


def endorsements(request):
    clients = Clients.objects.all()
    meta = MetaTags.objects.filter(page_name='endorsements').first()
    context = {'clients': clients, 'meta': meta}
    context.update(static_query())
    return render(request, 'endorsement/home.html', context)
