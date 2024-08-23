from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *

def index(request):
    return HttpResponse("OK!")

def home(request):
    products = Product.objects.all()
    
    prices = [product.price for product in products]
    names = [product.name for product in products]

    context = {
        "products": products,
        "price": prices,
        "name": names,
    }

    return render(request, "home.html", context)

def fruits(request):
    return HttpResponse("fruits")

def base(request):
    return render(request, "base.html", {})