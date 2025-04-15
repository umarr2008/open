from django.views.generic import View
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from shop.models import Product
from .models import Order, OrderItem, Coupon


class AddCouponView(View):

    def post(self, request, *args, **kwargs):
        coupon_code = request.POST.get('coupon_code')
        coupon = Coupon.objects.get(code=coupon_code)
        order = Order.objects.filter(user=request.user, ordered=False).first()
        order.coupon = coupon
        order.save()
        return redirect("cart")


class AddToCartView(View):

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        order_item, created = OrderItem.objects.get_or_create(
            product=product,
            user=request.user,
            ordered=False,
        )
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.items.filter(product__id=product_id).exists():
                order_item.quantity += 1
                order_item.save()
            else:
                order.items.add(order_item)
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
        return redirect("cart")


class CartView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        order_items = OrderItem.objects.filter(user=request.user, ordered=False)
        order = Order.objects.filter(user=request.user, ordered=False).first()
        context = {
            'order_items': order_items,
            'order': order
        }
        return render(request, 'order/cart.html', context)

    def post(self, request, *args, **kwargs):
        if request.POST.get('action') == 'add_coupon':
            coupon_code = request.POST.get('coupon_code')
            coupon = Coupon.objects.get(code=coupon_code)
            order = Order.objects.filter(user=request.user, ordered=False).first()
            order.coupon = coupon
            order.save()
        elif request.method == 'POST':
            order = Order.objects.filter(user=request.user, ordered=False).first()
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()
            order_items = OrderItem.objects.filter(user=request.user, ordered=False)
            for item in order_items:
                item.ordered = True
                item.save()

        return redirect("checkout")


class CheckoutView(LoginRequiredMixin, FormView):
    success_url = reverse_lazy('cart')
    form_class = None

    def get(self, request, *args, **kwargs):
        order_items = OrderItem.objects.filter(user=request.user, ordered=True)
        order = Order.objects.filter(user=request.user, ordered=True).first()
        context = {
            'order_items': order_items,
            'order': order
        }
        return render(request, 'order/checkout.html', context)
