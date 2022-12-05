from django.db import models


class SlideShow(models.Model):
    message = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    image = models.ImageField(upload_to='slide_show/images/')


class Service(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)

class Selected_Title(models.Model):
    title = models.CharField(max_length=256)
    banner = models.CharField(max_length=256)

class Activity(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    image = models.ImageField(upload_to='slide_show/images/')

class Person(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=256)
    role = models.CharField(max_length=256)
    Social_Id = models.CharField(max_length=256)

class Blog(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='slide_show/images/')
    text = models.CharField(max_length=256)

class Contant_Us(models.Model):
    WebAddress = models.URLField()
    email = models.EmailField()
    telephone = models.IntegerField()
    Address = models.CharField(max_length=256)

class Message(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    title = models.CharField(max_length=256)
    message = models.CharField(max_length=256)