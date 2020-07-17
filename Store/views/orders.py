from django.views import View
from django.shortcuts import redirect, render
from django.core import serializers
from Store.models.product import Product
from Store.models.orders import Orders as modelorder
from Store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


class Orders(View):

    def get_deserialized_object(self, data):
        for ob in serializers.deserialize("json", data):
            return ob.object

    @method_decorator(auth_middleware)
    def get(self, request):
        data = request.session.get('customer')
        customer = self.get_deserialized_object(data)
        orders = modelorder.get_orders_by_customer_id(customer)
        return render(request, 'orders.html', {'orders': orders})
