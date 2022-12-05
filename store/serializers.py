from rest_framework import serializers

from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=("id","name")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('title','author','description','image','slug','price','is_active')
    
    
class CategoryBasedProducts(serializers.ModelSerializer):
    product=ProductSerializer(many=True,read_only=True)
    class Meta:
        model=Category
        fields=('name','product')

   