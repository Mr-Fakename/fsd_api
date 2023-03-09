from django.db import models
from django.conf import settings


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('BlogCategory', on_delete=models.CASCADE, default=1)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts', null=True
    )
    image = models.ImageField(upload_to='blog/images/', blank=True)

    class Meta:
        verbose_name_plural = 'Blog Posts'
        ordering = ['-date_created']

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Blog Comments'
        ordering = ['-date']

    def __str__(self):
        return self.title


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Blog Categories'

    def __str__(self):
        return self.name

