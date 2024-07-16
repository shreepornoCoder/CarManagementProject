from django.db import models
from django.utils.text import slugify

class CarBrandModel(models.Model):
    brand_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.brand_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.brand_name