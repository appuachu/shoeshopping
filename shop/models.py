from django.db import models
from django.urls import reverse
# Create your models here.

class categ(models.Model):
    def __str__(self):
        return self.name


    def get_url(self):
        return reverse('prod_cat', args=self.slug)

    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'







#create a class for product section

class product(models.Model):
    def __str__(self):
        return self.name

    name=models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    detial= models.TextField(max_length=100, unique=True)
    price= models.IntegerField()
    image=models.ImageField(upload_to='static')
    disc=models.TextField(max_length=10000)
    stock=models.IntegerField()
    available=models.BooleanField
    category=models.ForeignKey(categ,on_delete=models.CASCADE)

class collections(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    prices=models.IntegerField()
    img=models.ImageField(upload_to='static')


#There are two keys primery key-it ia an unique key and forgin key



class placeorder(models.Model):
    def __str__(self):
        return self.firstname
    firstname=models.CharField(max_length=60)

    email=models.TextField(max_length=40)
    address=models.TextField(max_length=200)
    mobile=models.TextField(max_length=100)
    city=models.CharField(max_length=40)
    state=models.CharField(max_length=50)
    zip=models.IntegerField()
