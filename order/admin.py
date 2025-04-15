from django.contrib import admin

from order.models import Address, Coupon, OrderItem, Order

# Register your models here.
admin.site.register(Address)
admin.site.register(Coupon)
admin.site.register(OrderItem)
admin.site.register(Order)
