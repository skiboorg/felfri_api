
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from rest_framework import generics
from .models import *

class Pagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 10000
class GetTags(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
class GetNews(generics.ListAPIView):
    pagination_class = Pagination
    serializer_class = NewsItemShortSerializer
    def get_queryset(self):
        queryset = NewsItem.objects.all()
        tag = self.request.query_params.get('tag', None)
        print(tag)
        if tag:
            queryset = queryset.filter(tag__slug=tag)
        return queryset

class GetNewsItem(generics.RetrieveAPIView):
    serializer_class = NewsItemSerializer
    queryset = NewsItem.objects.filter()
    lookup_field = 'slug'
