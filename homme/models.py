from distutils.command import upload
from socketserver import ForkingMixIn
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Settings(models.Model):
    whoweare =models.CharField(max_length=200,null=False)
    whatwedo =models.CharField(max_length=200,null=False)
    whywedoit =models.CharField(max_length=200,null=False)
    sincewhen =models.CharField(max_length=200,null=False)
    address = models.CharField(max_length=200,null=False)
    mail=models.EmailField()
    phone=models.CharField(max_length=50)
class Header(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,null=False)
    subtitle=models.CharField(max_length=200,null=False)
class Skills(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,null=False)
    progress=models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
class Reviews(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,null=False)
    contient=models.CharField(max_length=200,null=False)
class Partners(models.Model):
    id=models.AutoField(primary_key=True)
    photo=models.ImageField(blank=True,upload_to="images/partners/")
class Fun(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,null=False)
    contient=models.CharField(max_length=200,null=False)
class Team(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False)
    photo=models.ImageField(blank=True,upload_to="images/team/")
    genre=models.CharField(max_length=10,null=False)
class TypeWorks(models.Model):
    id=models.CharField(max_length=20,primary_key=True)
class Works(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.ForeignKey("typeworks",on_delete=models.CASCADE)
    title=models.CharField(max_length=20,null=False)
    subtitle=models.CharField(max_length=100,null=False)
    photo=models.ImageField(blank=True,upload_to="images/works/")
    url=models.URLField(blank=True)


    

