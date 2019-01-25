from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .models import ContactModel, ContactSelling, Contact
from django.contrib import messages
from mainstreetbiz.views import static_query
from setting.models import SellYourBusiness
from .decorators import check_recaptcha


@check_recaptcha
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        is_valid = None
        if name and email and phone and message != '':
            is_valid = True
        else:
            is_valid = False
        if request.recaptcha_is_valid and is_valid:
            contact = Contact(name=name, email=email,
                              phone=phone, message=message)
            contact.save()
            subject = '{} ({}) wants to contact you'.format(name, email)
            send_mail(subject, message, 'info@mainstreetbiz.ca',
                      ('itzmk108@gmail.com',))
            messages.success(
                request, 'Your request has been submitted, a realtor will get back to you soon')

            return redirect('/contact')
        else:
            messages.error(
                request, 'Please enter valid details')

    return render(request, 'contact/contact.html', static_query())


@check_recaptcha
def contactSelling(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        type_of_business = request.POST['business_type']
        message = request.POST['message']

        is_valid = None
        if name and email and phone and city and message != '':
            is_valid = True
        else:
            is_valid = False

        if request.recaptcha_is_valid and is_valid:
            contact = ContactSelling(name=name, email=email, phone=phone, city=city,
                                     type_of_business=type_of_business, message=message)
            contact.save()
            subject = '{} ({}) wants to contact you'.format(name, email)
            send_mail(subject, message, 'info@mainstreetbiz.ca',
                      ('itzmk108@gmail.com',))
            messages.success(
                request, 'Thank you for your message, we will get back to you soon')

            return redirect('/contact/sell-your-business')
        else:
            messages.error(
                request, 'Please enter valid details')

    sellingpage = SellYourBusiness.objects.filter().first()
    context = {'sellingpage': sellingpage}
    context.update(static_query())
    return render(request, 'contact/sell-your-business.html', context)


def contactModel(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        business = request.POST['listing_title']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        is_valid = None
        if listing_id and business and name and email and message != '':
            is_valid = True
        else:
            is_valid = False

        if request.recaptcha_is_valid and is_valid:
            contact = ContactModel(listing_id=listing_id, business=business, name=name,
                                   email=email, phone=phone, message=message)

            contact.save()
            subject = '{} ({}) wants to contact you, regarding listing id {}'.format(
                name, email, listing_id)
            send_mail(subject, message, 'info@mainstreetbiz.ca',
                      ('itzmk108@gmail.com',))
            messages.success(
                request, 'Your request has been submitted, a realtor will get back to you soon')

            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(
                request, 'Please enter valid details')
