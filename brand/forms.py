from django import forms 
from brand.models import CarBrandModel

class BrandClass(forms.ModelForm):
    class Meta:
        model = CarBrandModel
        fields = ['brand_name']