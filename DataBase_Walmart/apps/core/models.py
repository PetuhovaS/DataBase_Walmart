from django.contrib.auth.models import User
from django.db import models



class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upc = models.CharField(max_length=16)
    image = models.CharField(max_length=200, blank=True) # не добавлено в БД и не прописано
    name = models.CharField(max_length=128, blank=True)
    brand = models.CharField(max_length=64, blank=True, null=True)
    model = models.CharField(max_length=32, blank=True)
    qty = models.CharField(max_length=8, default=0, null=True)
    in_stock = models.CharField(max_length=32, blank=True, default=0)
    price = models.DecimalField(max_digits=32, decimal_places=2, blank=True, default=0, null=True)
    free_shipping = models.BooleanField(max_length=32, blank=True,)
    date_updated = models.DateField(auto_now=False, auto_now_add=True, blank=True, null=True)



class Userdata(models.Model):
    api_key = models.CharField(max_length=128, default=None, null=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)






















