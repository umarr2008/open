from django.db import models

from shop.models import Product
from users.models import User


# Create your models here.
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address_line_1}, {self.city}, {self.country}"

    class Meta:
        verbose_name_plural = "Addresses"
        ordering = ["-id"]


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    discount = models.IntegerField()

    def __str__(self):
        return self.code


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    size = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)

    ordered = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_item_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s order"

    def get_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.get_total_item_price()
        return total

    def get_total_price_with_coupon(self):
        total = self.get_total_price()
        if self.coupon:
            total -= self.coupon.discount
        return total
