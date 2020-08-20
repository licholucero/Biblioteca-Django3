from django.db import models

# Create your models here.

class Libro(Material):
    editorial = models.CharField(max_length=40)
    fotoPortada = models.ImageField(max_length=100, upload_to='portadas/', blank=True)