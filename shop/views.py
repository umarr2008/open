from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from shop.forms import ProductReviewForm
from shop.models import Product, ProductCategory, ProductImage, ProductReview, Blog 
# Create your views here.

class HomePageView(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['expensive_products'] = Product.objects.all().order_by('-price')[0:8]  # eng qimmat mahsulotlar
        context['recent_products'] = Product.objects.all().order_by('-id')[0:8]  # eng so'ngi mahsulotlar
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['search_product'] = self.request.GET.get('search')
        if context['search_product']:
            context['products'] = Product.objects.filter(name__contains=context['search_product'])
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/detail.html'
    context_object_name = 'product'

    # form = ProductReviewForm
    #
    # if request.method == 'POST':
    #     form = ProductReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request, 'shop/detail.html', {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImage.objects.filter(product=self.object)
        context['related_products'] = Product.objects.filter(category=self.object.category).exclude(id=self.object.id)
        context['form'] = ProductReviewForm()
        return context
