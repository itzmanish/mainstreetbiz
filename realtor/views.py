from django.shortcuts import render
from .models import Realtor
from mainstreetbiz.views import static_query
from setting.models import MetaTags


def team(request):
    realtors = Realtor.objects.all()
    meta = MetaTags.objects.filter(page_name='our-team').first()
    context = static_query()
    context.update({'realtors': realtors, 'meta': meta})
    return render(request, 'about/team.html', context)
