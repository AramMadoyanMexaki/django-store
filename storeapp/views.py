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
        weight = float(request.POST["weight"])
        photo = request.FILES.get("photo")

        if photo:
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                return render(request, "add_product.html", {"error": "Category does not exist"})

            product = Product.objects.create(name=name, price=price, category=category, add_weight=weight, photo=photo)

        else:
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                return render(request, "add_product.html", {"error": "Category does not exist"})

            product = Product.objects.create(name=name, price=price, category=category, add_weight=weight)

        return redirect('home')

    return render(request, "add_product.html", {})


def buy(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        weight = float(request.POST["weight"])

        if weight <= product.add_weight:
            product.buy_weight = weight
            product.save()
            return render(request, "buy.html", {"id": product.id, "success": "the product is purchased.", "product": product})

        return render(request, "buy.html", {"message": "There is not enough product in stock.", "id": product.id, "product": product})

    return render(request, "buy.html", {"product": product})


def login(request):
    pass


def register(request):
    pass
