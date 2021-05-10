from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rollno = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(110000000),
            MinValueValidator(100000000)
        ], unique=True)
    dob = models.DateField()
    block = models.CharField(max_length = 2, choices=(("1", "A"),
    ("2", "B"),
    ("3", "C"),
    ("4", "D"),), default="1")
    roomno = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(999),
            MinValueValidator(0)
        ])
    phone = PhoneNumberField()
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return str(self.rollno)