from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from django.shortcuts import redirect


# Create your views here.

def login(request):

    return render(request,'accounts/login.html')

def register(request):
    if request.method =="POST":
        print("SUBMITTED")
        return redirect('register')
    else:
        return render(request,'accounts/register.html')

def dashboard(request):

    return render(request,'accounts/dashboard.html')

def logout(request):

    return render(request,'accounts/logout.html')
