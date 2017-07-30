#blog/models.py
from django.db import models
from django.urls import reverse

#건의사항
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


#댓글 모델
class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=250)

#게시판 모델
class Board(models.Model):
    subject =models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    created_date = models.DateField(null=True, blank=True)
    memo =models.TextField()
    hits = models.IntegerField(default=0, blank=True )