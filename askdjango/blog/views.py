from django.shortcuts import render,redirect
from django.shortcuts import render_to_response

from django.http import HttpResponse
from blog.models import Scrapping
from blog.models import Emart
from blog.models import Handling
from blog.models import Handling2
from blog.models import Handling3
from blog.models import Rice_E
from blog.models import Rice_L
from blog.models import Water_E
from blog.models import Water_L
from blog.models import Tissue_E
from blog.models import Tissue_L

from .forms import PostForm
from .forms import CheckForm
from .models import Post
from .models import Check


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

def factor(request):
    return render(request, 'blog/factor.html')

def select(request):
    return render(request, 'blog/select.html')

def writing(request):
    return render(request, 'blog/writing.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        # pylint: disable=E1101
        handling2s_rice = Handling2.objects.filter(title1__icontains=q)
        handling3s_rice = Handling3.objects.filter(title1__icontains=q)

        handling2s_water = Handling2.objects.filter(title2__icontains=q)
        handling3s_water = Handling3.objects.filter(title2__icontains=q)

        handling2s_tissue = Handling2.objects.filter(title3__icontains=q)
        handling3s_tissue = Handling3.objects.filter(title3__icontains=q)
        return render_to_response('blog/search.html',
            {'handling2s_rice': handling2s_rice, 'handling3s_rice': handling3s_rice, 
            'handling2s_water': handling2s_water, 'handling3s_water': handling3s_water,
            'handling2s_tissue': handling2s_tissue, 'handling3s_tissue': handling3s_tissue,
            'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def crawling_result_rice(request):
     # pylint: disable=E1101
    crawlings_E=Rice_E.objects.all().order_by('price')[:3]
    crawlings_L=Rice_L.objects.all().order_by('price')[:3]
    context={'crawlings_E': crawlings_E, 'crawlings_L': crawlings_L}
    return render(request, 'blog/crawling_result_rice.html',context)

def crawling_result_water(request):
     # pylint: disable=E1101
    crawlings_E=Water_E.objects.all().order_by('price')[:3]
    crawlings_L=Water_L.objects.all().order_by('price')[:3]
    context={'crawlings_E': crawlings_E, 'crawlings_L': crawlings_L}
    return render(request, 'blog/crawling_result_water.html',context)

def crawling_result_tissue(request):
     # pylint: disable=E1101
    crawlings_E=Tissue_E.objects.all().order_by('price')[:3]
    crawlings_L=Tissue_L.objects.all().order_by('price')[:3]
    context={'crawlings_E': crawlings_E, 'crawlings_L': crawlings_L}
    return render(request, 'blog/crawling_result_tissue.html',context)

def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=Post()
            post.title=form.cleaned_data['title']
            post.content=form.cleaned_data['content']
            post.save()
            print(form.cleaned_data)
        else:
            form.errors
        #방법 2)
        '''
          post =Post(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
          post.save()
        '''
        #방법 3)
        '''
           post=Post.objects.create(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
        '''
        #방법 4)
        '''
           post=Post.objects.create(**form.cleaned_data)
        '''
        return redirect('/blog/')
        
    else:
        form =PostForm()
    return render(request, 'blog/writing.html', {'form': form}, )

def recommend(request):
    if request.method =='POST':
        form = CheckForm(request.POST, request.FILES)
        if form.is_valid():
            check=Check()
            check.rice=form.cleaned_data['rice']
            check.water=form.cleaned_data['water']
            check.tissue=form.cleaned_data['tissue']
            
            a={'rice':form.cleaned_data['rice'],'water': form.cleaned_data['water'],'tissue':form.cleaned_data['tissue']}
            checkings=[]
            marts=[]
            # 선택 항목이 True 인 key 만 chenking[]에 넣기
            for x in a.keys():
                 if a.get(x) ==True:
                     checkings.append(x)
            marts.append(comparing(checkings)) #추천 마트 string 전달받기
            check.save()
            #print(form.cleaned_data)
        else:
            form.errors
        return render(request, 'blog/recommend_result.html', {'checkings':checkings, 'marts':marts})
    else:
        form =CheckForm()
    return render(request, 'blog/recommend.html',{'form': form},)

def recommend_result(request):
    return render(request, 'blog/recommend_result.html')

# recommend 함수에서 전달 받은 키 값을 가지고 최저가 계산 후, 마트를 추천해주는 함수
def comparing(a):
    re = Rice_E.objects.all().order_by('price')[:1]
    we = Water_E.objects.all().order_by('price')[:1]
    te = Tissue_E.objects.all().order_by('price')[:1]
    rl = Rice_L.objects.all().order_by('price')[:1]
    wl = Water_L.objects.all().order_by('price')[:1]
    tl = Tissue_L.objects.all().order_by('price')[:1]
    sum_E=0
    sum_L=0
    
    for x in range(len(a)):
      if str(a[x])=='rice':
           sum_E += int(re[0].price)
           sum_L += int(rl[0].price)
      if str(a[x])=='water':
           sum_E += int(we[0].price)
           sum_L += int(wl[0].price)
      if str(a[x])=='tissue':
           sum_E += int(te[0].price)
           sum_L += int(tl[0].price)
    
    if sum_E > sum_L:
        return 'emart'
    else:
        return 'lotte_mart'
        











