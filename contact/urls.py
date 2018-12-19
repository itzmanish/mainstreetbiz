from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('model', views.contactModel, name='contact_model'),
    path('sell-your-business', views.contactSelling, name='contact_for_sell'),
    path('', views.contact, name='contact')
]
