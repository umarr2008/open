from django.urls import path

from .views import AddToCartView, CartView, CheckoutView, AddCouponView

urlpatterns = [
    path('cart-create/', AddToCartView.as_view(), name='cart-create'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add_coupon'),

]
