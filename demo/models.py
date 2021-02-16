from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=40, blank=False, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    published = models.DateField(null=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)
