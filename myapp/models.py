from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Biodata(models.Model):
    name = models.CharField(max_length=52)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Enter a valid mobile number.")],
        unique=True
    )
    docs = models.FileField(upload_to='documents/')
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    region = models.CharField(max_length=30)
    program = models.CharField(max_length=30)

    def __str__(self):
        return self.name