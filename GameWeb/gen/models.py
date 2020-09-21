from django.db import models

# Create your models here.
class Action(models.Model):
    img1=models.ImageField(upload_to='image/')
    t1=models.CharField(max_length=30)
    t2=models.CharField(max_length=2000)

    def __str__(self):
        return self.t1

class Aventure(models.Model):
    img1=models.ImageField(upload_to='image/')
    t1=models.CharField(max_length=30)
    t2=models.CharField(max_length=2000)

    def __str__(self):
        return self.t1

class Role(models.Model):
    img1=models.ImageField(upload_to='image/')
    t1=models.CharField(max_length=30)
    t2=models.CharField(max_length=2000)

    def __str__(self):
        return self.t1

class Sport(models.Model):
    img1=models.ImageField(upload_to='image/')
    t1=models.CharField(max_length=30)
    t2=models.CharField(max_length=2000)

    def __str__(self):
        return self.t1