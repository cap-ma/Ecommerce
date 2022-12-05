from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Category, Product

from rest_framework import generics

from .serializers import CategorySerializer,CategoryBasedProducts

def product_all(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})

class CategoryList(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ProductListCaegoryBased(generics.ListAPIView):
    
    serializer_class=CategoryBasedProducts
    def get_queryset(self):
        category_name=self.kwargs['name']

        return Category.objects.filter(name=category_name)
        

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/single.html', {'product': product})
# Create your views here.

