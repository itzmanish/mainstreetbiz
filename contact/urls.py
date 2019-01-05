from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('model', views.contactModel, name='contact_model'),
    path('', views.contact, name='contact')
]
