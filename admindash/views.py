from django.shortcuts import render, redirect
from core.models import * 
from core.forms import InquiryForm
from catalogue.models import *
from catalogue.forms import ProductForm


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# ----------------------------------------------------------------------------- 
#              Inquiry submission by Anon User
# -----------------------------------------------------------------------------

def createInquiry(request, id):
    inquiryRaw= InquiryForm(request.POST or None)
    print("Inquiry form "+ str(inquiryRaw.errors))
    if inquiryRaw.is_valid():
        inquiry = inquiryRaw.save(commit=False)
        inquiry.product=Product.objects.get(id=id)
        inquiry.save()
        # subject = 'Inquiry by ' + request.POST['full_name'] + ' ' + request.POST['email']
        # message= request.POST['notes']
        # print(send_mail(
        #     subject, 
        #     message, 
        #     'info@printpoint.io', 
        #     ['subaiyalshk@gmail.com','subaiyalshk@printpoint.io', 'mahin.tariq@printpoint.io', 'sufiyanshk@printpoint.io', 'm.tariqshk@printpoint.io'], 
        #     fail_silently=False,
        #     ))
        return render(render, 'thankyou.html')
    context ={
        'inquiryForm':inquiryRaw
    }
    return render (request, 'inquiry.html', context)

# ----------------------------------------------------------------------------- 
#              Admin Dashboard Views
# -----------------------------------------------------------------------------

@login_required(login_url='/accounts/login')
def inquiries_view(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    context={
        'inquiries': Inquiry.objects.all()
    }
    return render(request, 'inquires.html', context)

@login_required(login_url='/accounts/login')
def dashboard(request):
    catalogues= Collection.objects.all()
    catalogueList=[]
    totalInquiries=0
    for catalogue in catalogues:
        productList=[]
        for product in catalogue.products.all():
            product_inquiries= product.inquiries.count()
            totalInquiries+=product_inquiries
            productList.append({
                'name':product.title,
                'inquiry_count':product_inquiries
                })
            
        catalogueList.append({
            'name':catalogue.name, 
            'description': catalogue.description,
            'featured' : catalogue.featured.all(), 
            'totalInquiries': totalInquiries,
            'products': productList
            })
    context = {'catalogues': catalogueList, 'totalInquiries': totalInquiries}
    return render(request, 'dashboard.html', context)

def user_logout(request):
    logout(request)
    return redirect ('/')

# def user_login(request):
#     print(request.POST)
#     if request.method == "GET":
#         context={
            
#         }
#         return render(request, 'login.html', context)
#     username = request.POST['login_username']
#     password = request.POST['login_password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect ('/office/dashboard')
#     else:
#         context={
#             'error':'invalid credentials'
#         }
#         return render(request, 'login.html', context)

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username= form.cleaned_data['username']
#             password=form.cleaned_data['password1']
#             user= authenticate(username=username, password=password)
#             login(request, user)
#             return redirect ('index')
#     else:
#         form = UserCreationForm()
#     context = {'form' : form }
#     return render(request, 'registration/register.html', context)


# ---------------------------------------------------------------------------- 
#               Catalogue CRUD
# ----------------------------------------------------------------------------
def catalogue_view(request, name):
    this_catalogue= Collection.objects.get(name=name)
    this_catalogue_products= this_catalogue.products.all()
    form = ProductForm()
    print(str(this_catalogue.name))
    context={
        'catalogue': this_catalogue,
        'products': this_catalogue_products,
        'form': form
    }
    return render(request, 'adminCatalogue.html', context)

# ---------------------------------------------------------------------------- 
#               Product/service CRUD
# ----------------------------------------------------------------------------
@login_required(login_url='/accounts/login')
def productCreate(request, name):
    this_catalogue = Collection.objects.get(name=name)
    this_catalogue_products= this_catalogue.products.all()
    form = ProductForm(request.POST, request.FILES or None)
    if form.is_valid():
        product= form.save(commit=False)
        product.catalogue=this_catalogue
        product.save()
        return redirect('admin_catalogue', name)
    context ={
        'form': form,
        'products': this_catalogue_products,
        'catalogue': this_catalogue,
    }
    return render(request, 'adminCatalogue.html', context)

@login_required(login_url='/accounts/login')
def productUpdate(request, id, name):
    product = Product.objects.get(id=id)
    this_catalogue = Collection.objects.get(name=name)
    form = ProductForm(request.POST or None, instance=product)
    inquiryForm= InquiryForm()
    if form.is_valid():
        product= form.save(commit=False)
        product.catalogue=this_catalogue
        product.save()
    context = {
        'product':product,
        "form": form,
        'inquiryForm':inquiryForm,
        'catalogue':this_catalogue
    }
    return render(request, "editProduct.html", context)

@login_required(login_url='/accounts/login')
def productDelete(request, id, name):
    Product.objects.get(id=id).delete()
    return redirect('admin_catalogue', name)  
