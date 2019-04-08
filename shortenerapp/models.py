from django.db import models
from .utils import short_url_creator


class URLShortener(models.Model):
    url = models.CharField(max_length=300)
    short_url = models.CharField(max_length=30, null=True, unique=True, blank=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.short_url is None or self.short_url == "":
            self.short_url = short_url_creator(self)
        super(URLShortener, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def show_url(self):
        return "https://shorturlcreator.herokuapp.com/{short_url}".format(short_url=self.short_url)