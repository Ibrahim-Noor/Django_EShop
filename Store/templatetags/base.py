from django import template
from django.core import serializers

register = template.Library()


@register.filter(name='get_name')
def get_name(request):
    data = request.session.get('customer')
    if data:
        for customer in serializers.deserialize("json", data):
            return(customer.object.full_name)
    return None
