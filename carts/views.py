from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "cart.html", {"cart": cart_obj})


def cart_update(request):
    print(request.POST)
    product_id = request.POST.get('product')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Product not found")
            return redirect('gocart')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)

    # return redirect(product_obj.get_absolute_url())
    return redirect('gocart')


def checkout_page(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "checkout.html", {"cart": cart_obj})


def order_confirmed_page(request):
    return render(request, "placed_order.html")
