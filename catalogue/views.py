from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import *

from core.forms import InquiryForm

# Create your views here.
def catalogue_view(request, name):
    catalogue= Collection.objects.get(name=name)
    context={
        'catalogueName':catalogue.name,
        'catalogueDescription':catalogue.description,
        'products': catalogue.products.all()
    }
    return render(request, 'catalogue.html', context)

def product_detail_view(request, id):
    this_product= Product.objects.get(id=id)
    photos = ProductImage.objects.filter(product=this_product)
    inquiryForm= InquiryForm()
    context={
        'photos': photos,
        'product': this_product,
        'inquiryForm':inquiryForm
    }
    return render(request, 'product_detail.html', context)

def productCreate(request):
    form = ProductForm(request.POST or None)
    inquiryForm= InquiryForm()
    if form.is_valid():
        form.save()
        return redirect("/catalogue")
    context ={
        'form': form,
        'inquiryForm':inquiryForm
    }
    return render(request, "createProduct.html", context)

def productUpdate(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    inquiryForm= InquiryForm()
    if form.is_valid():
        form.save()
    context = {
        "form": form,
        'inquiryForm':inquiryForm
    }
    return render(request, "editProduct.html", context)

def productDelete(request, id):
    Product.objects.get(id=id).delete()
    return redirect("/catalogue")  

