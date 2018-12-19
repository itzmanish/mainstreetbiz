from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import state_choices, price_choices, businessType_choices
# Create your views here.
from mainstreetbiz.views import static_query


def index(request):
    listings = Listing.objects.order_by(
        '-created_at').filter(is_published=True)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)
    context = {
        'list': paged_listing,
        'state': state_choices,
        'price': price_choices,
        'business_type_choice': businessType_choices
    }
    context.update(static_query())
    return render(request, 'listing/home.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-created_at')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords, title__icontains=keywords)

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
        'state': state_choices,
        'price': price_choices,
        'business_type_choice': businessType_choices,
        'values': request.GET
    }
    context.update(static_query())
    return render(request, 'listing/search.html', context)


def single_listing(request, slug):
    property = get_object_or_404(Listing, slug=slug)
    context = {'property': property}
    context.update(static_query())
    return render(request, 'listing/single_list.html', context)


def sold(request):
    property = Listing.objects.order_by(
        '-created_at').filter(status__status__iexact='sold')
    context = {'list': property}
    context.update(static_query())
    return render(request, 'listing/sold.html', context)
