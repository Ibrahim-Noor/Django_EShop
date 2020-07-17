from Store.models.category import Category
from Store.models.product import Product
from django.shortcuts import redirect, render
from django.core import serializers
from django.views import View
from django.http import request


class Index(View):
    def get(self, request, **kwargs):
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_id(categoryID)
        else:
            products = Product.get_all_products()
        data = {'products': products, 'categories': categories}
        return render(request, 'index.html', data)

    def post(self, request):
        product = request.POST.get("productID")
        remove = request.POST.get("remove")
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    quantity = quantity - 1
                    if quantity <= 0:
                        del cart[product]
                    else:
                        cart[product] = quantity
                else:
                    quantity = quantity + 1
                    cart[product] = quantity
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('homepage')
