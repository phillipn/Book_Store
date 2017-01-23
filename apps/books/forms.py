from django import forms

from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'author']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['rating', 'review']
