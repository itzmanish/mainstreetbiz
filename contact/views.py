from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .models import ContactModel, ContactSelling, Contact
from django.contrib import messages
from mainstreetbiz.views import static_query
from setting.models import SellYourBusiness


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email, phone=phone, message=message)

        contact.save()
        subject = '{} ({}) wants to contact you'.format(name, email)
        send_mail(subject, message, 'info@mainstreetbiz.ca',
                  ('itzmk108@gmail.com',))
        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon')

        return redirect('/contact')

    return render(request, 'contact/contact.html', static_query())


def contactSelling(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        type_of_business = request.POST['business_type']
        message = request.POST['message']

        contact = ContactSelling(name=name, email=email, phone=phone, city=city,
                                 type_of_business=type_of_business, message=message)

        contact.save()
        subject = '{} ({}) wants to contact you'.format(name, email)
        send_mail(subject, message, 'info@mainstreetbiz.ca',
                  ('itzmk108@gmail.com',))
        messages.success(
            request, 'Thank you for your message, we will get back to you soon')

        return redirect('/contact/sell-your-business')
    sellingpage = SellYourBusiness.objects.filter().first()
    context = {'sellingpage': sellingpage}
    context.update(static_query())
    return render(request, 'contact/sell-your-business.html', context)


def contactModel(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing_title = request.POST['listing_title']
        listing_slug = request.POST['listing_slug']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = ContactModel(listing_id=listing_id, listing_title=listing_title, name=name,
                               email=email, phone=phone, message=message)

        contact.save()
        subject = '{} ({}) wants to contact you, regarding listing id {}'.format(
            name, email, listing_id)
        send_mail(subject, message, 'info@mainstreetbiz.ca',
                  ('itzmk108@gmail.com',))
        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon')

        return redirect('/listings/'+listing_slug)
