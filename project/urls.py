from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from cars.views import BuyCarView
from cars.views import BuyCar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('profile/', views.profile, name="profile"),
    path('buyCar/<int:id>', BuyCar, name="buyCar"),
    path('logout/', views.Userlogout, name="logout"),
    path('profile/update_profile/<int:pk>/', views.UpdateUserProfile.as_view(), name="update_profile"),
    path('profile/change_password/', views.ChangePassView.as_view(), name="change_pass"),
    path('<slug:category_slug>/', views.home, name='category_wise_post'),
    path('cars/', include('cars.urls')),
    path('brand/', include('brand.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)