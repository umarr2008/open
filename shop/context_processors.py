from shop.models import Product


def products_context(request):
    products = Product.objects.all()
    return {'products': products}
