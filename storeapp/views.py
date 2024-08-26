from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_list_or_404
from .models import *


def index(request):
    products = Product.objects.all()
    
    prices = [product.price for product in products]
    names = [product.name for product in products]

    context = {
        "products": products,
        "price": prices,
        "name": names,
    }

    return render(request, "home.html", context)


def fruits_page(request):
    try:
        fruits = Product.objects.filter(category__name="Fruits")
    except Product.DoesNotExist:
        raise Http404("No Product matches the given query.")

    return render(request, "fruits_page.html", {"fruits": fruits})


def vegetables_page(request):
    try:
        vegetables = Product.objects.filter(category__name="Vegetables")
    except Product.DoesNotExist:
        raise Http404("No Product matches the given query.")
    
    return render(request, "vegan.html", {"vegetables": vegetables})


def add_product(request):
    pass


def login(request):
    pass


def meat(request):
    pass


def register(request):
    pass