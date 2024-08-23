from django.urls import path
from storeapp import views


urlpatterns = [
    path('', views.index, name="home"),
    path('fruits/', views.fruits, name="fruits"),
    path('base/', views.base, name="base"),
    path('home/', views.home, name="home"),
]
