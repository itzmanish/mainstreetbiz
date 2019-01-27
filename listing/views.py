from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import BusinessListing, CompletedDeals, CommercialListing
from .choices import price_choices
# Create your views here.
from mainstreetbiz.views import static_query


# For filter options

area_choices = []
businessType_choices = []


def filterSelection(BusinessListing={}, CommercialListing={}, business_category={}):
    global area_choices
    global businessType_choices
    area_choices = []
    businessType_choices = []

    # area_choices = list(set(k['area'] for k in area_list))

    if business_category == 'business':
        business_listings = BusinessListing.objects.values()
        if business_listings:
            businessType_choices = list(
                set(k['business_type'] for k in business_listings))
            area_choices = list(set(k['location'] for k in business_listings))
    elif business_category == 'commercial':
        commercial_listings = CommercialListing.objects.values()
        if commercial_listings:
            businessType_choices = list(
                set(k['business_type'] for k in commercial_listings))
            area_choices = list(set(k['location']
                                    for k in commercial_listings))
    else:
        businessType_choices = []
        area_choices = []


# for filter option
listings = BusinessListing.objects.order_by('-created_at')


def business(request):
    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    filterSelection(BusinessListing=BusinessListing,
                    business_category='business')
    context = {
        'list': paged_listing,
        'area': area_choices,
        'price': price_choices,
        'business_type_choice': businessType_choices,
        'form_action_url': '/business-listings/search/'
    }
    context.update(static_query())
    return render(request, 'listing/business.html', context)


def search_business(request):
    queryset_list = listings

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                Q(business__icontains=keywords) | Q(description__icontains=keywords))

    # for city
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            queryset_list = queryset_list.filter(
                location__icontains=area)
    # # for State
    # if 'state' in request.GET:
    #     state = request.GET['state']
    #     if state:
    #         queryset_list = queryset_list.filter(
    #             state__iexact=state)
    # for Business type
    if 'business_type' in request.GET:
        business_type = request.GET['business_type']
        if business_type:
            queryset_list = queryset_list.filter(
                business_type__icontains=business_type)
    # for price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                asking_price__lte=price, asking_price__gte=int(price)-100000)
    context = {
        'list': queryset_list,
        'area': area_choices,
        'price': price_choices,
        'business_type_choice': businessType_choices,
        'values': request.GET,
        'form_action_url': '/business-listings/search/'
    }
    context.update(static_query())
    return render(request, 'listing/business.html', context)


def single_business(request, listing_id):
    property = get_object_or_404(BusinessListing, listing_id=listing_id,)
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
    listings = CommercialListing.objects.order_by('-created_at')
    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    filterSelection(CommercialListing=CommercialListing,
                    business_category='commercial')
    context = {
        'list': paged_listing,
        'area': area_choices,
        'price': price_choices,
        'business_type_choice': businessType_choices,
        'form_action_url': '/commercial-listings/search/'
    }
    context.update(static_query())
    return render(request, 'listing/commercial.html', context)


def single_commercial(request, listing_id):
    property = get_object_or_404(CommercialListing, listing_id=listing_id)
    context = {'property': property}
    context.update(static_query())
    return render(request, 'listing/single_commercial_list.html', context)


def search_commercial(request):
    queryset_list = CommercialListing.objects.order_by('-created_at')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                Q(business__icontains=keywords) | Q(description__icontains=keywords))

    # for city
    if 'area' in request.GET:
        area = request.GET['area']
        if area:
            queryset_list = queryset_list.filter(
                location__icontains=area)
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
                business_type__icontains=business_type)
    # for price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                asking_price__lte=price, asking_price__gte=int(price)-100000)
    context = {
        'list': queryset_list,
        'area': area_choices,
        'price': price_choices,
        'business_type_choice': businessType_choices,
        'values': request.GET,
        'form_action_url': '/commercial-listings/search/'
    }
    context.update(static_query())
    return render(request, 'listing/commercial.html', context)
