from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.

class Category(BaseModel):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category_image=models.ImageField(upload_to='categories')

    def save(self,*args,**kwargs):
        self.slug=slugify(self.category_name)
        super(Category,self).save(*args,**kwargs)
    def __str__(self):
        return self.category_name
class ColorVarient(BaseModel):
        color_name=models.CharField(max_length=100)
        price=models.IntegerField(default=0)

        def __str__(self):
             return self.color_name
        

class SizeVarient(BaseModel):
        size_name=models.CharField(max_length=100)
        price=models.IntegerField(default=0)

        def __str__(self):
             return self.size_name

class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    price = models.IntegerField()
    product_description=models.TextField()
    color=models.ManyToManyField(ColorVarient,blank=True)
    size=models.ManyToManyField(SizeVarient,blank=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.product_name)
        super(Product,self).save(*args,**kwargs)
    def __str__(self):
        return self.product_name
    
class ProductImage(BaseModel):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_images')
    image=models.ImageField(upload_to='product')

