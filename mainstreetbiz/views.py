from django.shortcuts import render, redirect
from realtor.models import LegalDisclaimer, PrivacyPolicy
from listing.models import BusinessListing, FeaturedListing
from setting.models import SocialLink, Home, Contact, BuyingProcess, About, BusinessFinance, SellingProcess
from news.models import News
from django.db.models import Count


def static_query():
    social = SocialLink.objects.filter().first()
    contact = Contact.objects.filter().first()
    context = {
        'social': social,
        'contact': contact
    }
    return context


def home(request):
    home = Home.objects.filter().first()
    featured = FeaturedListing.objects.all()
    news = News.objects.order_by(
        '-created_At').annotate(Count('title'))[:3]
    context = {
        'home': home,
        'featured_item': featured,
        'latest_news': news
    }
    context.update(static_query())
    return render(request, 'home/home.html', context)


def legalDisclaimer(request):
    disclaimer = LegalDisclaimer.objects.filter().first()
    context = {'disclaimer': disclaimer}
    context.update(static_query())
    return render(request, 'home/legal-disclaimer.html', context)


def privacyPolicy(request):
    privacyPolicy = PrivacyPolicy.objects.filter().first()
    context = {'privacyPolicy': privacyPolicy}
    context.update(static_query())
    return render(request, 'home/privacy-policy.html', context)


def buyingProcess(request):
    buying = BuyingProcess.objects.filter().first()
    context = {'buying': buying}
    context.update(static_query())
    return render(request, 'home/buying-process.html', context)


def sellingProcess(request):
    selling = SellingProcess.objects.filter().first()
    context = {'selling': selling}
    context.update(static_query())
    return render(request, 'home/selling-process.html', context)


def about(request):
    about = About.objects.filter().first()
    context = {'about': about}
    context.update(static_query())
    return render(request, 'about/about.html', context)


def businessFinance(request):
    finance = BusinessFinance.objects.filter().first()
    context = {'finance': finance}
    context.update(static_query())
    return render(request, 'home/business-finance.html', context)
