from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.type

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(null=True,upload_to='static/images/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.description
