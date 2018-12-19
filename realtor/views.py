from django.shortcuts import render
from .models import Realtor
from mainstreetbiz.views import static_query


def team(request):
    realtors = Realtor.objects.all()
    context = static_query()
    context.update({'realtors': realtors, })
    return render(request, 'about/team.html', context)
