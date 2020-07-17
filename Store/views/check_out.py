from django.views import View
from django.shortcuts import redirect
from django.core import serializers
from Store.models.product import Product
from Store.models.orders import Orders


class Check_out(View):
    def get_deserialized_object(self, data):
        for ob in serializers.deserialize("json", data):
            return ob.object

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = self.get_deserialized_object(
            request.session.get('customer'))
        cart = request.session.get('cart')
        product_ids = list(cart.keys())
        products = Product.get_products_by_id(product_ids)
        # print(address, phone, customer.id, cart, products)

        for product in products:
            order = Orders(customer=customer,
                           product=product,
                           quantity=cart.get(str(product.id)),
                           price=product.price,
                           address=address,
                           phone=phone)

            order.place_order()

        request.session['cart'] = {}

        return redirect('cart')
