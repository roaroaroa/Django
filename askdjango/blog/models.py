#blog/models.py
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title= models.CharField(max_length=100)  #길이제한이 있는 문자열
    content= models.TextField()              #길이제한이 없는 문자열 for 기능성을 위하 타이트하게
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog:post_detail', arg=[self.id])

class Check(models.Model):
     rice=models.BooleanField()
     water=models.BooleanField()
     tissue=models.BooleanField()

class Scrapping(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
       return self.title

class Emart(models.Model):
    title= models.CharField(max_length=100, blank=True)
    price=models.CharField(max_length=20, blank=True)

class Handling(models.Model):
    title= models.CharField(max_length=300) 
    max_value=models.CharField(max_length=300,blank=True)
    title1= models.CharField(max_length=300) 
    min_value=models.CharField(max_length=300,blank=True)

#이마트에서 
class Handling2(models.Model):
     title1= models.CharField(max_length=300) 
     min_order1=models.CharField(max_length=300,blank=True)
     title2= models.CharField(max_length=300) 
     min_order2=models.CharField(max_length=300,blank=True)
     title3= models.CharField(max_length=300) 
     min_order3=models.CharField(max_length=300,blank=True)

#롯데마트에서 
class Handling3(models.Model):
     title1= models.CharField(max_length=300) 
     min_order1=models.CharField(max_length=300,blank=True)
     title2= models.CharField(max_length=300) 
     min_order2=models.CharField(max_length=300,blank=True)
     title3= models.CharField(max_length=300) 
     min_order3=models.CharField(max_length=300,blank=True)

   

class Discount(models.Model):
    title=models.CharField(max_length=100, blank=True)
    discount=models.CharField(max_length=100, blank=True)

class Rice_E(models.Model):
    title= models.CharField(max_length=100, blank=True)
    price=models.CharField(max_length=20, blank=True)
    

class Rice_L(models.Model):
    title= models.CharField(max_length=100, blank=True)
    price=models.CharField(max_length=20, blank=True)
    
    

class Water_E(models.Model):
    title= models.CharField(max_length=100, blank=True)
    price=models.CharField(max_length=20, blank=True)
    
    

class Water_L(models.Model):
    title= models.CharField(max_length=100, blank=True)
    price=models.CharField(max_length=20, blank=True)
    


class Tissue_E(models.Model):
    title= models.CharField(max_length=100, blank=True)
    price=models.CharField(max_length=20, blank=True)
    


class Tissue_L(models.Model):
    title= models.CharField(max_length=100, blank=True)
    price=models.CharField(max_length=20, blank=True)
   
