from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=40, blank=False, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    published = models.DateField(auto_now=False, auto_now_add=False, blank=True, default=0)
    is_published = models.BooleanField(default=0)
    cover = models.ImageField(upload_to="covers/", height_field=None, width_field=None, max_length=100, blank=True)
