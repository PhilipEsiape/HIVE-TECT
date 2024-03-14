from order_items.serializers import OrderItemSerializer
from User. models import User
from User.serializers import UserSerializer
from .models import Order
from rest_framework import serializers
from order_items.models import OrderItem
from carts.models import Cart 



class OrderSerializer(serializers.ModelSerializer):
          order_items = OrderItemSerializer(many=True)
          class Meta:
              model = Order 
              fields = [
                     'user',
                     'customer_name',
                     'customer_phone',
                     'address',
                     'pin_code',
                     'building_type',
                     'city',
                     'state',
                     'total_price',
                     'total_qty',
                     'order_items'
              ]
          def create(self, validated_data):
              order_items = validated_data.pop('order_items')
              order = Order.objects.create(**validated_data)
              for item in order_items:
                   OrderItem.objects.create(**item, order=order)
                   Cart.objects.filter(product=item['product'], user=validated_data['user']).delete()
                   return order


class OrderListSerializer(serializers.ModelSerializer):
      order_items = OrderItemSerializer(many=True)

      class Meta:
            model = Order
            fields = [
            'user',
            'customer_name',
            'customer_phone',
            'address',
            'pin_code',
            'building_type',
            'city',
            'state',
            'total_price',
            'total_qty',
            'order_items'
            ]                          