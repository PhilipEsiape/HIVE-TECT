from django.db import models
from User.models import User
from products.models import Product
# Create your models here.


class Cart(models.Model):
    
    class Meta(object):
        db_table = 'cart'

    user = models.ForeignKey(
        User, related_name='related_user', on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name='related_product', on_delete=models.CASCADE
    )
    quantity = models.IntegerField (
        'Quantity', blank=False, null=False, default=1
    )          

    @property
    def total_price(self):
        return self.quantity * self.product.price