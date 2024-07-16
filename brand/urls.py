from django.urls import path, include
from . import views
 
urlpatterns = [
    path('brand/', views.AddCarBrandView.as_view(), name='brand_url'),
]
