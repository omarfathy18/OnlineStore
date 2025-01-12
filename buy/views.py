from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from items.models import items
from buy.models import buy

# Create your views here.


def buying(request):
    if 'user' in request.session:
        email = request.session['user']
        cart = buy.objects.filter(email=email)
        price = buy.objects.filter(email=email, p_state=0).all()
        total = 0
        items = 0
        for i in price:
            prices = int(str(i).split()[4])
            total = total + prices
            quantities = int(str(i).split()[3])
            items = items + quantities
        return render(request, 'buy/buy.html', {'cart': cart, 'total': total, 'items': items})
    else:
        messages.error(request, 'Please login first')
        return redirect('login')


def done(request):
    email = request.session['user']
    id = request.POST['id']
    update = str(buy.objects.filter(id=id)[0])
    list1 = update.split()
    if list1[2] == '2':
        messages.error(request, 'The order is already canceled')
        return redirect('buying')
    else:
        cart = buy()
        cart.id = id
        cart.email = email
        cart.p_name = list1[0]
        cart.p_price = list1[1]
        cart.p_state = 1
        cart.p_quantity = list1[3]
        cart.p_total = list1[4]
        cart.p_img = list1[5]
        cart.save()
        return redirect('buying')


def cancel(request):
    email = request.session['user']
    id = request.POST['id']
    update = str(buy.objects.filter(id=id)[0])
    list1 = update.split()
    if list1[2] == '1':
        messages.error(request, 'The order is already delivered')
        return redirect('buying')
    else:
        cart = buy()
        cart.id = id
        cart.email = email
        cart.p_name = list1[0]
        cart.p_price = list1[1]
        cart.p_state = 2
        cart.p_quantity = list1[3]
        cart.p_total = list1[4]
        cart.p_img = list1[5]
        cart.save()
        return redirect('buying')


def logout(request):
    del request.session['user']
    return redirect('login')
