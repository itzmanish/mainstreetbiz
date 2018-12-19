from django.shortcuts import render, redirect
from realtor.models import LegalDisclaimer, PrivacyPolicy
from listing.models import Listing
from setting.models import SocialLink, Home, Contact, Buying, About


def static_query():
    social = SocialLink.objects.get()
    contact = Contact.objects.get()
    context = {
        'social': social,
        'contact': contact
    }
    return context


def home(request):
    home = Home.objects.get()
    context = {
        'home': home,
    }
    context.update(static_query())
    return render(request, 'home/home.html', context)


def legalDisclaimer(request):
    disclaimer = LegalDisclaimer.objects.get()
    context = {'disclaimer': disclaimer}
    context.update(static_query())
    return render(request, 'home/legal-disclaimer.html', context)


def privacyPolicy(request):
    privacyPolicy = PrivacyPolicy.objects.get()
    context = {'privacyPolicy': privacyPolicy}
    context.update(static_query())
    return render(request, 'home/privacy-policy.html', context)


def buying(request):
    buying = Buying.objects.get()
    context = {'buying': buying}
    context.update(static_query())
    return render(request, 'home/buying.html', context)


def about(request):
    about = About.objects.get()
    context = {'about': about}
    context.update(static_query())
    return render(request, 'about/about.html', context)
