from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=254)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=25)
    date = models.DateField()

    def __str__(self):
        return self.name

