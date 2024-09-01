from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
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


def category(request, cats):
    category = get_object_or_404(Category, name=cats)
    products = Product.objects.filter(category=category)

    if not products.exists():
        raise Http404("There are no products in that category")
    
    return render(request, "products.html", {"category": category.name, "products": products})


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        category_name = request.POST.get("category")
        photo = request.POST.get("photo")

        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            return render(request, "add_product.html", {"error": "Category does not exist"})

        Product.objects.create(name=name, price=price, category=category, photo=photo)

        return redirect('home')

    return render(request, "add_product.html", {})


def login(request):
    pass


def register(request):
    pass
