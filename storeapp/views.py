from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
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

        if request.user.is_authenticated:
            if weight <= product.add_weight:
                product.buy_weight = weight
                product.save()
                return render(request, "buy.html", {"id": product.id, "success": "the product is purchased.", "product": product})

            return render(request, "buy.html", {"message": "There is not enough product in stock.", "id": product.id, "product": product})

        return HttpResponseRedirect("/login/")
    
    return render(request, "buy.html", {"id": product.id, "product": product})


def _login(request):
    if request.method == "GET":
        return render(request, "login.html", {})

    password = request.POST["pass"]
    username = request.POST["username"]

    print("Entered password " + password + "\n" + "Entered username" + username)

    user = authenticate(request, username=username, password=password)
    print("User ", user)
    if user:
        login(request, user)
        return HttpResponseRedirect("/")
        
    return render(request, "login.html", {"error": "Failed to login to account"})


def register(request):
    if request.method == "GET":
        return render(request, "register.html", {})
    
    password = request.POST["pass"]
    email = request.POST["email"]
    username = request.POST["username"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]

    user = User.objects.create_user(
        password= password, 
        email=email, 
        first_name=first_name, 
        last_name=last_name, 
        username=username
    )

    user.save()

    return HttpResponseRedirect("/login/")


def _logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")
