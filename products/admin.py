from django.contrib import admin
from .models import Product
# Register your models here.


@admin.register(Product)
class ProductionModel(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'type', 'image', 'category']
    list_filter = []
    list_display = fields
    search_fields = ['name', 'description']      
