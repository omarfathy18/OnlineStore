from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from items.models import items
from buy.models import buy

# Create your views here.


def item(request):
    if request.POST:
        email = request.session['user']
        id = request.POST['id']
        quantity = request.POST['quantity']
        item_name = str(items.objects.filter(id=id)[0])
        list1 = item_name.split()
        total = int(quantity) * int(list1[1])
        cart = buy()
        cart.id = id
        cart.email = email
        cart.p_name = list1[0]
        cart.p_price = list1[1]
        cart.p_img = list1[2]
        cart.p_state = 0
        cart.p_quantity = quantity
        cart.p_total = total
        cart.save()
        return redirect('item')
    else:
        if 'user' in request.session:
            all_items = items.objects.all()
            return render(request, 'items/items.html', {'items': all_items})
        else:
            messages.error(request, 'Please login first')
            return redirect('login')


def logout(request):
    del request.session['user']
    return redirect('login')
