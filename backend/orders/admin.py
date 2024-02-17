from django.contrib import admin

from orders.models import Order
# Register your models here.


@admin.register(Order)
class OrderModel(admin.ModelAdmin):
          fields = ['user', 'customer_name', 'customer_phone', 'address', 'pin_code', 'building_type', 'city', 'state', 'total_price', 'total_qty']
          list_filter = []
          list_display = fields
          search_fields = ['user']