from django.shortcuts import render
from django.views.generic import CreateView
from brand.models import CarBrandModel
from brand.forms import BrandClass
from django.urls import reverse_lazy

# Create your views here.
class AddCarBrandView(CreateView):
    model = CarBrandModel
    form_class = BrandClass
    template_name = 'brand.html'
    success_url = reverse_lazy('homepage')
