import json
from decimal import Decimal

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class GetBanners(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class GetFaqs(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


