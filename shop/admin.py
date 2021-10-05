from django.contrib import admin
from . models import *
# Register your models here.
#create a class

class categadmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
admin.site.register(categ,categadmin)

#create a class for product

class productadmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock']
    list_editable = ['stock','price']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(product,productadmin)

class collectionadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(collections,collectionadmin)

class placeadmin(admin.ModelAdmin):
    list_display = ['firstname','mobile','email','address']
admin.site.register(placeorder,placeadmin)