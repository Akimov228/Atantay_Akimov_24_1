from django.shortcuts import render, redirect
from products.models import Product, Review
from products.forms import CreateProductForm, CreateReviewForm


PAGINATION_LIMIT = 3

def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search is not None:
            products = Product.objects.filter(
                title__icontains=search
            )

        max_page = products.__len__() // PAGINATION_LIMIT

        if round(max_page) < max_page:
            max_page = round(max_page) + 1

        if max_page < 1:
            max_page = 0

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'max_page': range(1, max_page+1)
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
                author=request.user,
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
    if request.method == 'GET' and not request.user.is_anonymous:
        context = {
            'form': CreateProductForm
        }
        return render(request, 'products/create.html', context=context)
    elif request.user.is_anonymous:
        return redirect('/products')


    if request.method == 'POST':
        form = CreateProductForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                author=request.user,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data['rate'] if form.cleaned_data['rate'] is not None else 5
            )
            return redirect('/products')







