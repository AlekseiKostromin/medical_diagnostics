from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from main.models import LabTest
from .cart import Cart
from .models import Cart, CartItem


@login_required()
def view_cart(request):
    #cart = request.user.cart
    cart = Cart.objects.all().filter(user=request.user).last()
    if not cart:
        cart = Cart.objects.create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    return render(request, 'cart/cart_list.html', {'cart_items': cart_items})


@login_required()
def cart_add(request, labtest_id):
    labtest = LabTest.objects.get(pk=labtest_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    try:
        cart_item = CartItem.objects.get(cart=cart, labtest=labtest)
        cart_item.quantity += 1
        cart_item.total = cart_item.price * cart_item.quantity
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(cart=cart, labtest=labtest, price=labtest.price)

    return redirect('main:labtest_list')


@login_required()
def increase_cart_item(request, labtest_id):
    labtest = LabTest.objects.get(pk=labtest_id)
    cart = request.user.cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, labtest=labtest)

    cart_item.quantity += 1
    cart_item.total = cart_item.price * cart_item.quantity


    cart_item.save()

    return redirect('cart:view_cart')


@login_required()
def decrease_cart_item(request, labtest_id):
    labtest = LabTest.objects.get(pk=labtest_id)
    cart = request.user.cart
    cart_item = cart.cartitem_set.get(labtest=labtest)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.total = cart_item.price * cart_item.quantity


        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart:view_cart')


@login_required()
def fetch_cart_count(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart = request.user.cart
        cart_count = CartItem.objects.filter(cart=cart).count()
    return JsonResponse({'cart_count': cart_count})


def get_cart_count(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart=request.user.cart)
        cart_count = cart_items.count()
    else:
        cart_count = 0
    return cart_count


def get_total_price(self):
    return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
