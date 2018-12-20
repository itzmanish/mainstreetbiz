from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('', views.business, name='business_listing'),
    path('search/', views.search_business, name='business_search'),
    path('<slug:slug>/', views.single_business, name='business_listing_single'),
]
