import django_filters
from django.forms.widgets import TextInput
from django_filters import CharFilter, RangeFilter, ModelChoiceFilter
from .models import *
from django import forms


class Name_And_Price_Filter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    price = RangeFilter(field_name='price', lookup_expr='icontains')
    tags = ModelChoiceFilter(queryset=Tag.objects.all())
    brands = ModelChoiceFilter(queryset=Brand.objects.all(), label='Your name')

    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['image', 'digital']
