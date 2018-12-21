from django.urls import path
from .views import register, inventory
app_name = 'buyersregistry'

urlpatterns = [
    path('', inventory, name='buyers_inventory'),
    path('register/', register, name='buyers_registry')
]
