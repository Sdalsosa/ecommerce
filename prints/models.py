from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Print(models.Model):
    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, 
                                 on_delete=models.SET_NULL,
                                 related_name='prints')
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2,
                                validators=[MinValueValidator(0.00)],)
    image = models.ImageField(null=True, blank=True,)
    stock = models.IntegerField(default=0,
                                validators=[MinValueValidator(0)],)
    reprint = models.IntegerField(default=3, 
                                  validators=[MinValueValidator(0)],)
    likes = models.ManyToManyField(User, blank=True, 
                                   related_name='print_likes')

    def __str__(self):
        return self.name
