from django.shortcuts import render, redirect
from .models import Products, Order
from django.core.paginator import Paginator
from .froms import PlacedOrder
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


def detail(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product': product})

def checkout(request):
    form = PlacedOrder(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    # if request.method == "POST":
    #     items = request.POST.get('items',"")
    #     name = request.POST.get('name',"")
    #     email = request.POST.get('email',"")
    #     address = request.POST.get('address',"")
    #     city = request.POST.get('city',"")
    #     state = request.POST.get('state',"")
    #     zip = request.POST.get('zip',"")
    #     total = request.POST.get('total',"")

    #     order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zip=zip, total=total)
    #     order.save()
    return render(request, 'shop/checkout.html')