"""mainstreetbiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, legalDisclaimer, privacyPolicy, buying, about

urlpatterns = [
    path('', home, name='index'),
    path('legal-disclaimer/', legalDisclaimer, name='legal-disclaimer'),
    path('privacy-policy/', privacyPolicy, name='privacy-policy'),
    path('mainstreet/', admin.site.urls),
    path('buying/', buying, name='buying'),
    path('listings/', include('listing.urls')),
    path('blog/', include('blog.urls')),
    path('about/', about, name='about'),
    path('team/', include('realtor.urls')),
    path('contact/', include('contact.urls')),
    path('downloads/', include('downloads.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
