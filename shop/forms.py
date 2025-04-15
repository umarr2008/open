from django import forms
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['product', 'user', 'review', 'rating']
        widgets = {
            'product': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your review'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Your rating'})
        }
