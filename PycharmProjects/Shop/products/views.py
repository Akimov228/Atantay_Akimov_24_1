from django.shortcuts import render, redirect
from products.models import Product, Review
from products.forms import CreateProductForm, CreateReviewForm

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


def products_detail_view(request, product_id):
    if request.method == 'GET':
        product_obj = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product=product_obj)
        context = {
            'product': product_obj,
            'review': reviews,
            'form': CreateReviewForm

        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product_obj = Product.objects.get(id=product_id)
        reviews = Review.objects.filter(product=product_obj)
        form = CreateReviewForm(data=request.POST)

        if form.is_valid():
            Review.objects.create(
                product=product_obj,
                text=form.cleaned_data.get('text')
            )

            return redirect(f'/products/{product_obj.id}')

        return render(request, 'products/detail.html', context={
            'product': product_obj,
            'review': reviews,
            'form': form
        })



def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': CreateProductForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        form = CreateProductForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data['rate'] if form.cleaned_data['rate'] is not None else 5
            )
            return redirect('/products')







