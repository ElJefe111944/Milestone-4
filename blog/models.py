from django.db import models
from profiles.models import UserProfile
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=55)
   
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_detail')


class Post(models.Model):
    publish_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=55)
    title_tag = models.CharField(max_length=55)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    blog_image = models.ImageField(blank=True)
    subheading1 = models.TextField(
        max_length=55, null=False, blank=False, default="Subheading")
    main_content1 = models.TextField(
        max_length=255, null=False, blank=False, default="Main Content")
    subheading2 = models.TextField(max_length=55, null=True, blank=True)
    main_content2 = models.TextField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=55)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
