from urllib import response
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from django.http import HttpResponse
from django.contrib.auth import logout,login,authenticate




# Create your views here.





@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_page(request):
    if request.user.is_authenticated:
        return redirect(home_page)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            
            return redirect("/home")
        else:
            messages.info(request, "Invalid Username and Password")
            return redirect("/")

    else:
        return render(request, 'loginpage.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home_page(request):
    if request.user.is_authenticated:
        return render(request,"home.html")
    return redirect(login_page)


def logout_page(request):
    if request.user.is_authenticated:
        request.session.flush()
        
    return redirect(login_page)
