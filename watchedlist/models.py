from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.db import models

class User(AbstractUser):
    pass


class Item(models.Model):
    item_id = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lister", null=False, blank=False)
    comment = models.TextField(max_length=1000)
    rate = models.FloatField(null=True, blank=True)
    list = models.CharField(max_length=20, choices=(("watchlist","watchlist"),("watchedlist","watchedlist"), ("droppedlist","droppedlist")), null=False, blank=False)
    image_url = models.URLField(max_length=200, null=True, blank=True) # Add this line

    def __str__(self):
        return f"{self.title}"

