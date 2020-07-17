from django.db import models
from Store.models.customer import Customer
from Store.models.product import Product
import datetime


class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    address = models.CharField(
        max_length=300, default='', blank=True, null=True)
    phone = models.CharField(max_length=13, default='', blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customer_id(customer):
        return Orders\
            .objects\
            .filter(customer=customer.id).order_by('-date')
