from django.shortcuts import render
from .models import Category, Vendor
from django.views.generic.edit import CreateView

class CategoryCreateView(CreateView):
    model = 'Category'
    fields = ['name']
    template_name = 'templates/vendors/create_category.html'

class VendorCreateView(CreateView):
    model = 'Vendor'
    fields = ['name','description','location','category']
    template_name = 'tmplates/vendors/create_vendor.html'
