from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=1000, null = False, blank = False, unique = True)
    author = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE, related_name="posts")
    date_posted  = models.DateTimeField(default=timezone.now, null = False, blank = False)
    data = models.TextField(null = False, blank = False)
    slug = models.SlugField(null =True, blank = True, unique= True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Image(models.Model):
    image = models.ImageField(upload_to = "post_images")


class Comment(models.Model):
    post = models.ForeignKey(Post, null = False, blank = False, related_name = "comments", on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, null = False, blank = False)
    date_posted  = models.DateTimeField(default=timezone.now, null = False, blank = False)
    data = models.CharField(null = False, blank = False, max_length = 5000)


class SubComment(models.Model):
    comment = models.ForeignKey(Comment, null = False, blank = False, related_name = "sub_comments", on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, null = False, blank = False)
    date_posted  = models.DateTimeField(default=timezone.now, null = False, blank = False)
    data = models.CharField(null = False, blank = False, max_length = 5000)