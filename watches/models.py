from django.db import models

# Create your models here.

""" Primary = New, Secondary = Discount, Danger = Sold """ 
LABEL = (
    ('P', 'PRIMARY'), 
    ('S', 'SECONDARY'), 
    ('D', 'DANGER'), 
) 


class Brand(models.Model):
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Watch(models.Model):

    class Meta:
        verbose_name_plural = 'Watches'

    sku = models.CharField(max_length=254, null=True, blank=True)
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.FloatField(blank=True, null=True)
    label = models.CharField(
        choices=LABEL, max_length=20, default='SOME STRING')
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name