from django.urls import path
from .views import endorsements
app_name = 'endorsement'

urlpatterns = [
    path('', endorsements, name='endorsements')
]
