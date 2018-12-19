from django.urls import path
from . import views

app_name = 'realtor'

urlpatterns = [
    path('', views.team, name='team')
]
