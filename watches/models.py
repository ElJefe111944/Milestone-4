from django.db import models

# Create your models here.

""" Primary = New, Secondary = Discount, Danger = Sold """
LABEL = (
    ('New', 'New'),
    ('Discount', 'Discount'),
    ('Sold', 'Sold'),
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
    image = models.ImageField(null=True, blank=True)

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
    watch_information = models.TextField(default='BASIC INFORMATION')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.FloatField(blank=True, null=True)
    label = models.CharField(
        choices=LABEL, max_length=20,
        default='SOME STRING',
        blank=True, null=True
    )
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    watch = models.ForeignKey(
        Watch, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    review = models.TextField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.review
