#dojo/views.py
import os.path
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

def mysum(request, x):
    #request: HttpRequest
    return HttpResponse(x)


def hello(request, name, age):
    return HttpResponse('안녕하세요.{}.{}살이시네요.'.format(name,age))


def post_list1(request):
    name='공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>
    '''.format(name=name))


def post_list2(request):
    name='공유'
    return render(request, 'dojo/post_list.html', {'name': name})
   
def post_list3(request):
  
   
    return JsonResponse({
        'message': '안녕 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],

    },json_dumps_params={'ensure_ascii': False})

def excel_download(request):   
    filepath = "C:Users\sec\Desktop\github\Django\askdjango\gdplev.xls"  
    #settings.BASE_DIR
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')        
        # 필요한 응답헤더 세팅       
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)       
        return response
