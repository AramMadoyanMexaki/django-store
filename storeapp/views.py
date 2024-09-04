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
    
    context = {
        "category": category.name, 
        "products": products,
    }
    
    return render(request, "products.html", context)


def add_product(request):
    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        category_name = request.POST["category"]
        photo = request.FILES.get("photo")

        if photo:
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                return render(request, "add_product.html", {"error": "Category does not exist"})

            product = Product.objects.create(name=name, price=price, category=category, photo=photo)

        else:
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                return render(request, "add_product.html", {"error": "Category does not exist"})

            product = Product.objects.create(name=name, price=price, category=category)

        return redirect('home')

    return render(request, "add_product.html", {})


def buy(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "buy.html", {})


def login(request):
    pass


def register(request):
    pass
