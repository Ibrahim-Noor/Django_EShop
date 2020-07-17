from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    if str(product.id) in cart:
        return True
    return False


@register.filter(name='quantity_in_cart')
def quantity_in_cart(product, cart):
    if str(product.id) in cart:
        return cart.get(str(product.id))
    return 0


@register.filter(name='price_total')
def price_total(product, cart):
    if cart:
        return (product.price * cart.get(str(product.id)))
    return 0


@register.filter(name="total_cart_price")
def total_cart_price(products, cart):
    print("dsadsadsasdsadsa")
    sum = 0
    if cart:
        for p in products:
            sum += price_total(p, cart)
    return sum
