from django.contrib import admin
from cars.models import Add_Car, Comment, Buy_Car

# Register your models here.
admin.site.register(Add_Car)
admin.site.register(Comment)
admin.site.register(Buy_Car)