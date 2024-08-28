from urllib.parse import urlparse
from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    named_url = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)

        parsed_url = urlparse(self.url)
        return parsed_url.path

    def __str__(self):
        return self.name