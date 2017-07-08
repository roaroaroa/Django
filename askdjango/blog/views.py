from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Scrapping
from blog.models import Emart
from blog.models import Handling


def post_list(request):
    
    # pylint: disable=E1101
    #scrappings = Scrapping.objects.all()
    emarts = Emart.objects.all()
    
     
    #context = {'scrappings' : scrappings }
    context = {'emarts' : emarts}
    return render(request, 'blog/post_list.html', context) 

def index(request):
    return render(request, 'blog/index.html')

def handling(request):
    
    # pylint: disable=E1101
    handlings = Handling.objects.all()
    context = {'handlings': handlings}
    return render(request, 'blog/handling.html',context)

