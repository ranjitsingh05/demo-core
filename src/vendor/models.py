from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    joined = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name