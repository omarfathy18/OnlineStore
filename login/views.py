from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from login.models import users

# Create your views here.


def login(request):
    if request.POST:
        email = request.POST['email']
        real_email = users.objects.filter(email=email)
        if real_email:
            pwd = request.POST['pwd']
            real_pwd = users.objects.filter(email=email, pwd=pwd)
            if real_pwd:
                request.session['user'] = email
                return redirect('item')
            else:
                messages.error(request, 'Wrong password')
                return redirect('login')
        else:
            messages.error(request, 'Email not found')
            return redirect('login')
    else:
        return render(request, 'login/login.html')
