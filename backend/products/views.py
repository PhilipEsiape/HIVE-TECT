from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, serializers
from django_filters.rest_framework import DjangoFilterBackend
from User.mixins import CustomLoginRequiredMixin
from products.serializers import ProductSerializer
from rest_framework import filters

from .models import Product



class ProductList(CustomLoginRequiredMixin, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category_id', 'type']
    search_fields = ['name', 'description']     