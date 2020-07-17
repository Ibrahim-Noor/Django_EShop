from django.shortcuts import redirect


def cart_present_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.session.get('cart'):
            request.session['cart'] = {}

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
