from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="products/photos/", max_length=100, null=True, blank=True)
    price = models.IntegerField(default=0, verbose_name="Price kg")
    buy_weight = models.FloatField(default=0)
    add_weight = models.FloatField(null=True, blank=True)
    rest_weight = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        if self.add_weight is not None:
            self.rest_weight = self.add_weight - self.buy_weight
        else:
            self.rest_weight = 0

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class StoreUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    