from django.db import models

from profiles.models import UserProfile

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=55)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    body = models.TextField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
