from django.shortcuts import render, redirect
from mainstreetbiz.views import static_query
from .models import Register, BuyersDirectoryPage
from django.contrib import messages


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

        user = Register(first_name=first_name, last_name=last_name, email=email, phone=phone, business_type=business_type,
                        investment_type=investment_type, business_area=business_area, business_price=business_price, max_cash=max_cash, remarks=remarks)

        user.save()
        messages.success(
            request, 'You are successfully registered with us.')
        return redirect('/')

    return render(request, 'buyersregistry/register.html', static_query())


def inventory(request):
    buyers_directory = BuyersDirectoryPage.objects.filter().first()
    context = {'directory': buyers_directory}
    context.update(static_query())
    return render(request, 'buyersregistry/home.html', context)
