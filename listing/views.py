from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing, Area, Business_Type, CompletedDeals
from .choices import price_choices
# Create your views here.
from mainstreetbiz.views import static_query

area_choices = {}
businessType_choices = {}
listings = Listing.objects.order_by(
    '-created_at').filter(is_published=True, Type='business', )


def business(request):
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    global area_choices
    area_list = Area.objects.all()
    if area_list:
        for k in area_list:
            area_choices[k] = k
    else:
        area_choices = {}
    business_type = Business_Type.objects.all()
    global businessType_choices
    if business_type:
        for k in business_type:
            businessType_choices[k] = k
    else:
        businessType_choices = {}
    context = {
        'list': paged_listing,
        'area': area_choices,
        'price': price_choices,
        'business_type_choice': businessType_choices
    }
    context.update(static_query())
    return render(request, 'listing/business.html', context)


def search_business(request):
    queryset_list = listings

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                Q(title__icontains=keywords) | Q(description__icontains=keywords))

    # for city
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            queryset_list = queryset_list.filter(
                area__area__icontains=area)
    # # for State
    # if 'state' in request.GET:
    #     state = request.GET['state']
    #     if state:
    #         queryset_list = queryset_list.filter(
    #             state__iexact=state)
    # for Business type
    if 'business_type' in request.GET:
        business_type = request.GET['business_type']
        print(business_type)
        if business_type:
            queryset_list = queryset_list.filter(
                business_type__business_type__icontains=business_type)
    # for price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)
    context = {
        'list': queryset_list,
        'area': area_choices,
        'price': price_choices,
        'business_type_choice': businessType_choices,
        'values': request.GET
    }
    context.update(static_query())
    return render(request, 'listing/search.html', context)


def single_business(request, slug):
    property = get_object_or_404(
        Listing, slug=slug, Type='business', is_published=True,)
    context = {'property': property}
    context.update(static_query())
    return render(request, 'listing/single_business_list.html', context)


def completed(request):
    property = CompletedDeals.objects.order_by(
        '-completion')
    context = {'list': property}
    context.update(static_query())
    return render(request, 'listing/completed-deals.html', context)


def commercial(request):
    listings = Listing.objects.order_by(
        '-created_at').filter(is_published=True, Type='commercial',)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    context = {
        'list': paged_listing,
        'area': area_choices,
        'price': price_choices,
        'business_type_choice': businessType_choices
    }
    context.update(static_query())
    return render(request, 'listing/commercial.html', context)


def single_commercial(request, slug):
    property = get_object_or_404(
        Listing, slug=slug, Type='commercial', is_published=True, )
    context = {'property': property}
    context.update(static_query())
    return render(request, 'listing/single_commercial_list.html', context)


def search_commercial(request):
    queryset_list = Listing.objects.order_by(
        '-created_at').filter(Type='commercial', is_published=True)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                Q(title__icontains=keywords) | Q(description__icontains=keywords))

    # for city
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            queryset_list = queryset_list.filter(
                area__area__icontains=area)
    # # for State
    # if 'state' in request.GET:
    #     state = request.GET['state']
    #     if state:
    #         queryset_list = queryset_list.filter(
    #             state__iexact=state)
    # for Business type
    if 'business_type' in request.GET:
        business_type = request.GET['business_type']
        print(business_type)
        if business_type:
            queryset_list = queryset_list.filter(
                business_type__business_type__icontains=business_type)
    # for price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)
    context = {
        'list': queryset_list,
        'area': area_choices,
        'price': price_choices,
        'business_type_choice': businessType_choices,
        'values': request.GET
    }
    context.update(static_query())
    return render(request, 'listing/commercial_search.html', context)
