from django.shortcuts import render
from Store.models.product import Product
from django.views import View


class Cart(View):
    def get(self, request):
        cart = request.session.get('cart')
        if cart:
            product_ids = list(cart.keys())
            products = Product.get_products_by_id(product_ids)
            return render(request, 'cart.html', {'products': products})
        else:
            return render(request, 'cart.html', {'products': []})
