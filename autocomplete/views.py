from django.http import JsonResponse

from food_choice.models import Product


def complete(request):
    searched_term = request.GET.get("term")
    products = Product.objects.get_all_by_term(searched_term)
    products = [
        {
            "name": product.name[:32] + "..."
            if len(product.name) > 35
            else product.name,
            "id": product.id,
        }
        for product in products
    ]
    return JsonResponse(products, safe=False)
