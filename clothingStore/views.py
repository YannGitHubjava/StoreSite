from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from clothingStore.models import Product
import json


def index(request):
    last_prod = Product.pmg.all().order_by('-productID')[:4]

    context = {"last_prod": last_prod}
    print(context)
    return render(request, "home.html", context)




def about(request):

    return render(request, "about.html")


def product(request):
    products = Product.pmg.all()

    context = { "products": products}
    return render(request, "product.html", context)


