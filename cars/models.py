from django.db import models
from brand.models import CarBrandModel
from django.contrib.auth.models import User

# Create your models here.
class Add_Car(models.Model):
    car_name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    brand = models.ForeignKey(to=CarBrandModel, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="media/", blank=True, null=True)

    def __str__(self):
        return self.car_name

class Comment(models.Model):
    post = models.ForeignKey(to=Add_Car, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"Comment is Done By {self.name}"

class Buy_Car(models.Model):
    car = models.ForeignKey(to=Add_Car, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car.car_name} is bought by {self.user.username}"