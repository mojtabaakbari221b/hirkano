from django.db import models


class SlideShow(models.Model):
    message = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    image = models.ImageField()


class Service(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)