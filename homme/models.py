
from django.utils.safestring import mark_safe
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Setting(models.Model):
    whoweare =models.CharField(max_length=200,null=False)
    whatwedo =models.CharField(max_length=200,null=False)
    whywedoit =models.CharField(max_length=200,null=False)
    sincewhen =models.CharField(max_length=200,null=False)
    address = models.CharField(max_length=200,null=False)
    mail=models.EmailField()
    phone=models.CharField(max_length=50)
    file=models.FileField(blank=True,upload_to="setting/")
    def __str__(self) :
        return "setting"
class Header(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,null=False)
    subtitle=models.CharField(max_length=200,null=False)
    url=models.URLField(max_length=200,null=False,default="")
    def __str__(self):
        return self.title
class Skill(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,null=False)
    progress=models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
class Review(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,null=False)
    contient=models.CharField(max_length=200,null=False)
class Partner(models.Model):
    id=models.AutoField(primary_key=True)
    photo=models.ImageField(blank=True,upload_to="partners/")
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.photo.url if self.photo else "/media/partners/partner.png"))
class Fun(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,null=False)
    contient=models.CharField(max_length=200,null=False)
class Team(models.Model):
    class Genre(models.TextChoices):
        Man = 'MAN'
        Woman = 'WOMAN'
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False)
    photo=models.ImageField(blank=True,upload_to="teams/")
    genre=models.CharField(max_length=10,choices=Genre.choices,null=False)
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.photo.url if self.photo else "/media/teams/team.png"))
class Work(models.Model):
    id=models.AutoField(primary_key=True)
    type=models.CharField(max_length=20)
    title=models.CharField(max_length=20,null=False)
    subtitle=models.CharField(max_length=100,null=False)
    photo=models.ImageField(blank=True,upload_to="works/")
    url=models.URLField(blank=True)
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.photo.url if self.photo else "/media/teams/team.png"))
class Service(models.Model):
    id=models.AutoField(primary_key=True)
    icon=models.CharField(max_length=50)
    title=models.CharField(max_length=50,null=False)
    content=models.TextField(max_length=200,null=False)
    def __str__(self) :
        return self.title
    def show_icon(self):
        return mark_safe(''.format(self.icon))
class Characteristic(models.Model):
    characteristic=models.CharField(primary_key=True,max_length=200)
    def __str__(self) :
        return self.characteristic
class Subscribe(models.Model):
    email=models.EmailField(primary_key=True)
    def __str__(self) :
        return self.email
class Price(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,null=True)
    service=models.ForeignKey(Service,on_delete=models.CASCADE,null=True)
    icon=models.CharField(max_length=50)
    money=models.DecimalField(max_digits=10,decimal_places=2)
    characteristic=models.ManyToManyField(Characteristic,null=True)
    popular=models.BooleanField(default=False)
class Message(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.TextField(max_length=5000)
class CounterUp(models.Model):
    id=models.AutoField(primary_key=True)
    icon=models.CharField(max_length=50)
    title=models.CharField(max_length=50,null=False)
    count=models.IntegerField()
    def __str__(self) :
        return self.title
    def show_icon(self):
        return mark_safe(''.format(self.icon))