from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from online_shop.cart.forms import CartAddProductForm
from .recommender import Recommender

# paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


'''
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        "shop/product/list.html",
        {"category": category,
         "categories": categories,
         "products": products},
    )
'''

def product_list(request, category_slug=None):

    category = None
    object_list = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        object_list = object_list.filter(category=category)
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver first page
        products = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)

    return render(
        request,
        "shop/product/list.html",
        {"page":page,
         "category": category,
         "products": products},
    )












def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

    return render(
        request,
        "shop/product/detail.html",
        {"product": product,
         "cart_product_form": cart_product_form,
         'recommended_products': recommended_products},
    )


