from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('completed-deals/', views.sold, name='sold'),
    path('<slug:slug>/', views.single_listing, name='listing_single'),
]
