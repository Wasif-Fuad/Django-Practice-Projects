from django.shortcuts import render
from .models import Product
# Create your views here.
def product(request,slug):
    context={'product':Product.objects.get(slug=slug)}
    return render(request,'products/product.html',context)