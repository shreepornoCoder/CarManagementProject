from django.urls import path, include
from . import views
 
urlpatterns = [
    path('add_car/', views.AddCarView.as_view(), name='add_car_url'),
    path('cars/details/<int:id>/', views.DetailsPostView.as_view(), name='details_post'),
]
