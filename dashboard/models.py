from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Laundry(models.Model):
    date = models.DateField(default=timezone.now)
    rollno = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(110000000),
            MinValueValidator(100000000)
        ])
    tshirt = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    jeans = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    shorts = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    bedsheet = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    towel = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    shirts = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    hoodie = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    delivered = models.BooleanField(default = False)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rollno)
    
    def get_absolute_url(self):
        return reverse("dashboard-laundry")

class Menu(models.Model):
    meal = models.CharField(max_length = 9, choices=(("Breakfast", "Breakfast"),
    ("Lunch", "Lunch"),
    ("Dinner", "Dinner")), default="Breakfast")
    monday = models.CharField(max_length = 255)
    tuesday = models.CharField(max_length = 255)
    wednesday = models.CharField(max_length = 255)
    thursday = models.CharField(max_length = 255)
    friday = models.CharField(max_length = 255)
    saturday = models.CharField(max_length = 255)
    sunday = models.CharField(max_length = 255)

    def __str__(self):
        return str(self.meal)
    
