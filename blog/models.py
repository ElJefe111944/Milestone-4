from django.db import models
from profiles.models import UserProfile
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    publish_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=55)
    title_tag = models.CharField(max_length=55)
    info = models.CharField(max_length=155, default="Summary")
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    blog_image = models.ImageField(blank=True)
    subheading1 = models.TextField(
        max_length=55, null=False, blank=False, default="Subheading")
    main_content1 = models.TextField(
        max_length=355, null=False, blank=False, default="Main Content")
    subheading2 = models.TextField(
        max_length=55, blank=True, default="Subheading2")
    main_content2 = models.TextField(
        max_length=355, blank=True, default="Main Content2")
    subheading3 = models.TextField(
        max_length=55, blank=True, default="Subheading3")
    main_content3 = models.TextField(
        max_length=355, blank=True, default="Main Content3")
    main_content_extra = models.TextField(
        max_length=355, blank=True, default="Main Content Extra")
    likes = models.ManyToManyField(UserProfile, related_name='blog_posts')


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
