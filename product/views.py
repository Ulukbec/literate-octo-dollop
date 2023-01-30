from django.shortcuts import render, HttpResponse

from product.models import Product


# Create your views here.

def main_view(request):
    return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        data = {
            'products': products
        }
        return render(request, 'product/product.html', context=data)

def product(request):
    return HttpResponse(request, 'huia')