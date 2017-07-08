#blog/models.py
from django.db import models


class Post(models.Model):
    title= models.CharField(max_length=100)  #길이제한이 있는 문자열
    content= models.TextField()              #길이제한이 없는 문자열 for 기능성을 위하 타이트하게
    tags= models.CharField(max_length=100, blank=True)
    lngat= models.CharField(max_length=50, blank=True, help_text='위도/경도 포맷으로 ')
    created_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

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


class Discount(models.Model):
    title=models.CharField(max_length=100, blank=True)
    discount=models.CharField(max_length=100, blank=True)