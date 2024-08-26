from django.urls import path
from storeapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name="home"),
    path('fruits/', views.fruits_page, name="fruits"),
    path('vegetables/', views.vegetables_page, name="vegan"),
    path('meat/', views.meat, name="meat"),
    path('add_product/', views.add_product, name="add"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
