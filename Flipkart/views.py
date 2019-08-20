from flipkart import FlipkartAPI, Authentication
from django.http import JsonResponse


def get_orders(request):
    auth = Authentication('app id', 'app secret', sandbox=True)
    token = auth.get_token_from_client_credentials()
    flipkart = FlipkartAPI(token['access_token'], sandbox=True, debug=True)
    orders = flipkart.search_orders()
    return JsonResponse({
        'orders': orders
    })
