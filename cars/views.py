from django.shortcuts import render, redirect
from . import models
from . import forms
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views import View
from django.shortcuts import get_object_or_404
from cars.models import Add_Car, Buy_Car

# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddCarView(CreateView):
    model = models.Add_Car
    form_class = forms.AddCarForms
    template_name = "add_car.html"
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        print("Car Added")
        messages.success(self.request, "Car Added Successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Car did not Added")
        messages.warning(self.request, "Car Added UnSuccessfully!")
        return super().form_invalid(form)

class DetailsPostView(DetailView):
    model = models.Add_Car
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = forms.CommentForms(data=self.request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post 
            new_comment.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # saving post models object
        comments = post.comments.all()
        comment_form = forms.CommentForms()

        context['comments'] = comments
        context['comment_form'] = comment_form
        context['post'] = post
        return context

class BuyCarView:
    model = models.Buy_Car    
    pk_url_kwarg = 'id'
    template_name = 'profile.html'

    def post(self, request, *args, **kwargs):
        post = self.get_object()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context["post"] = post
        return context

def BuyCar(request, id):
    car = get_object_or_404(Add_Car, id=id)
    
    if car.quantity <= 0:
        messages.warning(request, "Stock Out")
        return redirect('profile')
    
    car.quantity -= 1
    car.save()

    Buy_Car.objects.create(user=request.user, car=car)
    messages.success(request, f"You have successfully bought {car.car_name}.")
    return redirect('profile')

class BuyCarView(View):
    def post(self, request, car_id):
        car = get_object_or_404(Add_Car, id=car_id)
        if car.quantity > 0:
            car.quantity -= 1
            print(car.quantity)
            car.save()
            Buy_Car.objects.create(user=request.user, car=car)
        return redirect('profile')
