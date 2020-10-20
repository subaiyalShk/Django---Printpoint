from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import InquiryForm
from catalogue.models import Collection
from django.core.mail import send_mail


def index(request):
    catalogueList=[]
    for catalogue in Collection.objects.all():
        print(str(catalogue.name))
        catalogueList.append({'featured' : catalogue.featured.all(), 'name':catalogue.name, 'description':catalogue.description})
    context = {'catalogues': catalogueList}
    return render(request, 'index.html', context)

def home(request):
    catalogueList=[]
    for catalogue in Collection.objects.all():
        print(str(catalogue.name))
        catalogueList.append({'featured' : catalogue.featured.all(), 'name':catalogue.name, 'description':catalogue.description})
    context = {'catalogues': catalogueList}
    return render(request, 'home.html', context)

def about(request):

    return render(request, 'about.html')

def contact(request):
    if request.method == "GET":
        return render(request, 'contact.html')
    elif request.method == "POST" :
        print(request.POST)
        subject = 'Inquiry by ' + request.POST['name'] + ' ' + request.POST['email']
        message= request.POST['message']
        send_mail(subject, 
            message, 
            'info@printpoint.io', 
            ['subaiyalshk@gmail.com', 'mahin.tariq@printpoint.io', 'sufyanshk@printpoint.io', 'm.tariqshk@printpoint.io'], 
            fail_silently=False,
            )
        return render(request, 'thankyou.html', {'message_sent':'True'})



