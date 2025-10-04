from django.shortcuts import render , get_object_or_404
from .models import category,Product


def product_list(request,category_slug=None):
    categories = category.objects.all()
    products = Product.objects.filter(available=True)

    category = None
    if category_slug:
        category = get_object_or_404(category, category_slug=category_slug)
        products = products.filter(category=category)

    return render(request,'main/product/list.html',
                  {'category' : category,
                  'categories' : categories,
                  'products': products})


# Create your views here.
