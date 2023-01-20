from django.shortcuts import HttpResponse,render
from products.models import Product, Review

def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }

        return render(request, 'products/products.html', context=context)


def products_detail_view(request, post_id):
    if request.method == 'GET':
        product = Product.objects.get(id=post_id)
        reviews = Review.objects.filter(product=product)
        context = {
            'product': product,
            'review': reviews
        }

        return render(request, 'products/detail.html', context=context)
