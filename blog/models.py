from django.db import models

from profiles.models import UserProfile

# Create your models here.


class Post(models.Model):
    publish_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=55)
    title_tag = models.CharField(max_length=55, default="Blog")
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    blog_image = models.ImageField(null=True, blank=True)
    introduction = models.TextField(
        max_length=55, null=False, blank=False, default="Introduction"), 
    subheading1 = models.TextField(
        max_length=55, null=False, blank=False, default="Subheading")
    main_content1 = models.TextField(
        max_length=255, null=False, blank=False, default="Main Content")
    subheading2 = models.TextField(max_length=55, null=True, blank=True)
    main_content2 = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
