from django.conf import settings
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=45)
    email = models.EmailField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=80)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']


class Setup(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='setups', null=True
    )
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Setups'
        ordering = ['name']
