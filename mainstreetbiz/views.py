from django.shortcuts import render, redirect
from realtor.models import LegalDisclaimer, PrivacyPolicy
from listing.models import BusinessListing, FeaturedListing
from setting.models import SocialLink, Home, Contact, BuyingProcess, About, BusinessFinance, SellingProcess, FooterImages, MetaTags
from feeds.models import FeedPost
from django.db.models import Count


def static_query():
    social = SocialLink.objects.filter().first()
    contact = Contact.objects.filter().first()
    footer_img = FooterImages.objects.all()
    context = {
        'social': social,
        'contact': contact,
        'footer_image': footer_img
    }
    return context


def home(request):
    home = Home.objects.filter().first()
    meta = MetaTags.objects.filter(page_name='home').first()
    featured = FeaturedListing.objects.all()
    news = FeedPost.objects.order_by(
        '-date').annotate(Count('title'))[:3]
    context = {
        'home': home,
        'featured_item': featured,
        'latest_news': news,
        'meta': meta
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
    meta = MetaTags.objects.filter(page_name='buying-process').first()
    context = {'buying': buying, 'meta': meta}
    context.update(static_query())
    return render(request, 'home/buying-process.html', context)


def sellingProcess(request):
    selling = SellingProcess.objects.filter().first()
    meta = MetaTags.objects.filter(page_name='selling-process').first()
    context = {'selling': selling, 'meta': meta}
    context.update(static_query())
    return render(request, 'home/selling-process.html', context)


def about(request):
    about = About.objects.filter().first()
    meta = MetaTags.objects.filter(page_name='about-business').first()
    context = {'about': about, 'meta': meta}
    context.update(static_query())
    return render(request, 'about/about.html', context)


def businessFinance(request):
    finance = BusinessFinance.objects.filter().first()
    meta = MetaTags.objects.filter(page_name='small-business-finance')
    context = {'finance': finance, 'meta': meta}
    context.update(static_query())
    return render(request, 'home/business-finance.html', context)
