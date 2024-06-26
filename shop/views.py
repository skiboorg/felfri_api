from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from rest_framework import generics
from .models import *

# class GetInstructions(APIView):
#     def get(self, request):
#         return Response("Hello World")

class GetInstructions(generics.ListAPIView):
    serializer_class = SubCategoryInstructuctionSerializer
    queryset = SubCategory.objects.all()
class GetCategories(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class GetCategory(generics.RetrieveAPIView):
    serializer_class = CategoryShortSerializer
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
    queryset = Product.objects.filter(is_popular=True, is_active=True)


class GetNewProducts(generics.ListAPIView):
    serializer_class = ProductShortSerializer
    queryset = Product.objects.filter(is_new=True, is_active=True)

class UpdateProducts(APIView):
    def post(self, request):
        data = request.data
        for item in data:
            product_qs = Product.objects.filter(article_num=item['article_num'])
            if product_qs.exists():
                product = product_qs.first()
                product.price = item['price_ozon']
                product.price_wb = item['price_wb']
                product.wb_link = item['link_wb'].replace('\/','/')
                product.ozon_link = item['link_ozon'].replace('\/','/')
                product.save()
        return Response(status=200)


class Test(APIView):

    def get(self, request):
        import requests
        data = [
            {
                "article_num": "11",
                "Наименование": "Утюг беспроводной IR-02",
                "link_wb": "https:\/\/www.wildberries.ru\/catalog\/216809775\/detail.aspx",
                "price_wb": 1617,
                "link_ozon": "https:\/\/ozon.ru\/context\/detail\/id\/1522019621\/",
                "price_ozon": 1765
            },
            {
                "article_num": "22",
                "Наименование": "Утюг проводной IR-01",
                "link_wb": "https:\/\/www.wildberries.ru\/catalog\/218775205\/detail.aspx",
                "price_wb": 1001,
                "link_ozon": "https:\/\/ozon.ru\/context\/detail\/id\/1547667211\/",
                "price_ozon": 702
            },
        ]
        re =requests.post('http://localhost:8000/api/shop/updatetable', json=data)
        return Response(status=200)