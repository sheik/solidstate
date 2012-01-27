from django.db import models

class Website(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

class Page(models.Model):
    website = models.ForeignKey(Website)
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True)

