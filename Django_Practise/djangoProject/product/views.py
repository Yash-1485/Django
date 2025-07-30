from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def product_list(request):
    # products=Product.objects.all()
    search_term=request.GET.get("search")
    if search_term:
        products=Product.objects.filter(name__icontains=search_term)
    else:
        products=Product.objects.all()
    return render(request,"product/product_list.html",{"products":products})

def product(request,id):
    product=Product.objects.get(pk=id)
    return render(request,"product/product.html",{"product":product})