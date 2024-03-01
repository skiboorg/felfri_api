from .serializers import *
from rest_framework import generics
from .models import *

class GetCategories(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class GetCategory(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()
    lookup_field = 'slug'

class GetSubCategory(generics.RetrieveAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.filter()
    lookup_field = 'slug'

class GetProduct(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter()
    lookup_field = 'slug'

class GetPopularProducts(generics.ListAPIView):
    serializer_class = ProductShortSerializer
    queryset = Product.objects.filter(is_popular=True)


class GetNewProducts(generics.ListAPIView):
    serializer_class = ProductShortSerializer
    queryset = Product.objects.filter(is_new=True)