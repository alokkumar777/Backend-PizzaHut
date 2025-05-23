from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Product

# Create your views here.
# request -> response
# request handler
# return render(req, 'index.html', {'data':data})

def productFetch(request):
    products = Product.objects.all().values()
    context = {
        'products': products
    }
    # first_product = products[0]
    return render(request, 'product.html', context)


def details(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, 'details.html', context)

def main(request):
    return render(request, 'main.html')

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)