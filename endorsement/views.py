from django.shortcuts import render
from mainstreetbiz.views import static_query
from .models import Clients


def endorsements(request):
    clients = Clients.objects.all()
    context = {'clients': clients}
    context.update(static_query())
    return render(request, 'endorsement/home.html', context)
