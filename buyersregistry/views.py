from django.shortcuts import render, redirect
from mainstreetbiz.views import static_query
from .models import Register, BuyersDirectoryPage
from django.contrib import messages
from contact.decorators import check_recaptcha
from setting.models import MetaTags


def user_exist(email):
    users = Register.objects.all()
    for user in users:
        user_existed = None
        if user.email == email:
            user_existed = True
        else:
            user_existed = False
    return user_existed


@check_recaptcha
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        business_type = request.POST['business_type']
        investment_type = request.POST['investment_type']
        business_area = request.POST['business_area']
        business_price = request.POST['business_price']
        max_cash = request.POST['max_cash']
        remarks = request.POST['remarks']

        is_valid = None
        if first_name and last_name and email and phone and business_area and business_price and business_type and investment_type and max_cash and remarks != '':
            is_valid = True
        else:
            is_valid = False

        if request.recaptcha_is_valid and is_valid and ',' not in business_price and ',' not in max_cash and user_exist(email):
            user = Register(first_name=first_name, last_name=last_name, email=email, phone=phone, business_type=business_type,
                            investment_type=investment_type, business_area=business_area, business_price=business_price, max_cash=max_cash, remarks=remarks)

            user.save()
            messages.success(
                request, 'You are successfully registered with us.')
            return redirect('/buyers-inventory/register/')
        else:
            if(user_exist(email)):
                messages.warning(
                    request, 'This email is already exists.')
            else:
                messages.error(
                    request, 'Please enter valid details.')
            return redirect('/buyers-inventory/register/')
    meta = MetaTags.objects.filter(
        page_name='buyers-directory-register').first()
    context = {'meta': meta}
    context.update(static_query())
    return render(request, 'buyersregistry/register.html', context)


def inventory(request):
    buyers_directory = BuyersDirectoryPage.objects.filter().first()
    meta = MetaTags.objects.filter(page_name='buyers-directory').first()
    context = {'directory': buyers_directory, 'meta': meta}
    context.update(static_query())
    return render(request, 'buyersregistry/home.html', context)
