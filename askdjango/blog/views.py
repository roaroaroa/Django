from django.shortcuts import render
from blog.models import Scrapping
from blog.models import Emart
from django.http import HttpResponse


def post_list(request):
    #scrappings = Scrapping.objects.all()
    emarts = Emart.objects.all()

    #context = {'scrappings' : scrappings }
    context = {'emarts' : emarts }
    return render(request, 'blog/post_list.html', context) 


