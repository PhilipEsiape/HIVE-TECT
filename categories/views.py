from rest_framework import generics
from categories.models import Category
from categories.serializers import CategorySerializer

# Create your views here.


class CategoryList(generics.ListAPIView):
          serializer_class = CategorySerializer
          queryset = Category.objects.all()
          pagination_class = None
