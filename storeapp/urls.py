from django.urls import path
from storeapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name="home"),
    path('category/<str:cats>', views.category, name="category"),
    path('add_product/', views.add_product, name="add"),
    path('login/', views._login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views._logout, name="logout"),
    path('buy/<int:id>/', views.buy, name="buy"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
