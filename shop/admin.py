from django.contrib import admin

from shop.models import ProductCategory, Product, ProductImage, ProductReview, Blog

admin.site.register(Blog)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
