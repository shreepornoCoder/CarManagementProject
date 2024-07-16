from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from brand.models import CarBrandModel
from cars.models import Add_Car
from django.shortcuts import render, get_object_or_404
from cars.forms import *
from . import forms
from cars.models import Buy_Car

def home(request, category_slug=None):
    data = Add_Car.objects.all()
    categories = CarBrandModel.objects.all()

    if category_slug:
        category = get_object_or_404(CarBrandModel, slug=category_slug)
        data = Add_Car.objects.filter(brand=category)

    return render(request, 'home.html', {'brand': categories, 'data': data})

@login_required
def profile(request):
    cars = Buy_Car.objects.filter(user=request.user)
    print(cars)
    return render(request, 'profile.html', {"cars":cars})

class SignUpView(CreateView):
    form_class = forms.RegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, "You Signed Up Successfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, "Signed Up UnSuccessful!")
        return super().form_invalid(form)

class LoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("homepage")

    def get_success_url(self):
        return reverse_lazy("homepage")

    def form_valid(self, form):
        messages.success(self.request, "You Logged In Successfully!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, "Logged In UnSuccessful!")
        return super().form_invalid(form)
    
@method_decorator(login_required, name="dispatch")
class UpdateUserProfile(UpdateView):
    model = User
    form_class = forms.ProfileUpdateForm
    template_name = "update_profile.html"

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "Account Updated Successfully!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Update Your Profile"
        return context

@method_decorator(login_required, name="dispatch")
class ChangePassView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "change_pass.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        messages.success(self.request, "Password Changed Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "UnSuccessful Operation!")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Change Your Password"
        return context

def Userlogout(request):
    logout(request)
    messages.success(request, "Logout Successfully!")
    return redirect('homepage')
