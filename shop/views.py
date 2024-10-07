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
            try:
                article_num = item.get('article_num',False)
                if article_num:

                    product_qs = Product.objects.filter(article_num=article_num)
                    if product_qs.exists():

                        product = product_qs.first()
                        print(product)
                        price_ozon = item.get('price_ozon','0')
                        price_wb = item.get('price_wb','0')
                        link_wb = item.get('link_wb','').replace('\/','/')
                        link_ozon = item.get('link_ozon','').replace('\/','/')



                        product.price = price_ozon
                        product.price_wb = price_wb
                        product.wb_link = link_wb
                        product.ozon_link = link_ozon

                        if int(product.price) > int(product.price_wb):
                            if int(product.price_wb) != 0:
                                product.show_price = product.price_wb
                            else:
                                product.show_price = product.price
                        else:
                            if int(product.price) != 0:
                                product.show_price = product.price
                            else:
                                product.show_price = product.price_wb


                        product.save()
            except:
                pass

        return Response(status=200)


class Test(APIView):

    def get(self, request):
        import requests
        data = [
            {
                "article_num": "asd123123",
                "Наименование": "Утюг беспроводной IR-02",
                 "link_wb": "https:\/\/www.wildberries.ru\/catalog\/216809775\/detail.aspx",
                 "price_wb": 3,
                 "link_ozon": "1https:\/\/ozon.ru\/context\/detail\/id\/1522019621\/",
                 "price_ozon": 26
            },
        ]
        response = requests.post('http://localhost:8000/api/shop/updatetable', json=data)
        print(response.text)
        return Response(status=200)