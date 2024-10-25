from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_object = Products.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != '' and item_name != None:
        product_object = Products.objects.filter(title__icontains = item_name)
        pass

    # Paginator
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    return render(request, 'shop/index.html', {'products' : product_object})