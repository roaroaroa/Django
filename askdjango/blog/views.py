from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.db.models import Q
from datetime import datetime
from django.http import HttpResponse
#크롤링 
from blog.models import Rice_E
from blog.models import Rice_L
from blog.models import Water_E
from blog.models import Water_L
from blog.models import Tissue_E
from blog.models import Tissue_L
#form
from .forms import PostForm
from .forms import CheckForm
from .models import Post
from .models import Check
from .forms import CommentForm
from .models import Comment
from .models import Board
from .forms import BoardForm
#그래프보여주기
import matplotlib as mpl
import matplotlib.pylab as plt 
from pylab import savefig
import numpy as np
#mysql 길이 산출 함수
from django.db.models.functions import Length
 
 
#메인 
def index(request):
    #댓글 기능
    if request.method =='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment =Comment()
            comment.name=form.cleaned_data['name']
            comment.content=form.cleaned_data['content']
            comment.save()
        else:
            form.errors
        return redirect('/blog/')
    else:
        form =CommentForm()
    
    comments= Comment.objects.all()
    return render(request, 'blog/index.html' , {'form': form, 'comments': comments} )



def select(request):
    return render(request, 'blog/select.html')

def writing(request):
    return render(request, 'blog/writing.html')
#검색하기 
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        # pylint: disable=E1101
        handling2s_rice = Rice_E.objects.filter(title__icontains=q)
        handling3s_rice = Rice_L.objects.filter(title__icontains=q)

        handling2s_water = Water_E.objects.filter(title__icontains=q)
        handling3s_water = Water_L.objects.filter(title__icontains=q)

        handling2s_tissue = Tissue_E.objects.filter(title__icontains=q)
        handling3s_tissue = Tissue_L.objects.filter(title__icontains=q)
        return render_to_response('blog/search.html',
            {'handling2s_rice': handling2s_rice, 'handling3s_rice': handling3s_rice, 
            'handling2s_water': handling2s_water, 'handling3s_water': handling3s_water,
            'handling2s_tissue': handling2s_tissue, 'handling3s_tissue': handling3s_tissue,
            'query': q})
    else:
        return HttpResponse('Please submit a search term.')
#각 마트의 최저가 3가지를 보여주는 함수
def crawling_result(request):
    title= request.GET['title']
    if title == 'rice':
      # pylint: disable=E1101
       crawlings_E=Rice_E.objects.all().order_by(Length('price'),'price')[:3]#price를 1,11,12,순서가 아니라 ,1,2,3 숫자정렬하기
       crawlings_L=Rice_L.objects.all().order_by(Length('price'),'price')[:3]
       context={'crawlings_E': crawlings_E, 'crawlings_L': crawlings_L}
       return render(request, 'blog/crawling_result.html',context)
      
    elif title =='water':
       crawlings_E=Water_E.objects.all().order_by(Length('price'),'price')[:3]
       crawlings_L=Water_L.objects.all().order_by(Length('price'),'price')[:3]
       context={'crawlings_E': crawlings_E, 'crawlings_L': crawlings_L}
       return render(request, 'blog/crawling_result.html',context)

    elif title =='tissue':
       crawlings_E=Tissue_E.objects.all().order_by(Length('price'),'price')[:3]
       crawlings_L=Tissue_L.objects.all().order_by(Length('price'),'price')[:3]
       context={'crawlings_E': crawlings_E, 'crawlings_L': crawlings_L}
       return render(request, 'blog/crawling_result.html',context)
#건의사항 접수
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
#추천하기 함수
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
def comparing(a):# 여기서 a는 사용자가 체크박스에서 선택한, 값이 TRUE인 튜플
    re = Rice_E.objects.all().order_by(Length('price'),'price')[:1] # 쌀 품목들의 최저가만
    we = Water_E.objects.all().order_by(Length('price'),'price')[:1]
    te = Tissue_E.objects.all().order_by(Length('price'),'price')[:1]
    rl = Rice_L.objects.all().order_by(Length('price'),'price')[:1]
    wl = Water_L.objects.all().order_by(Length('price'),'price')[:1]
    tl = Tissue_L.objects.all().order_by(Length('price'),'price')[:1]
    sum_E=0
    sum_L=0

    sum_E += min_value_E(a,re,'rice') # a 안에 rice가 있는지 확인하고 , 이마트 쌀의 최저가 산출
    sum_E += min_value_E(a,we,'water')
    sum_E += min_value_E(a,te,'tissue')
    sum_L += min_value_L(a,rl,'rice') 
    sum_L += min_value_L(a,wl,'water')
    sum_L += min_value_L(a,tl,'tissue') #여기가 까지 계산하면, 사용자가 체크박스에서 선택한 값들의 최저가 합이
                                        #smu_E와 sum_L에 들어간다.
    '''
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
    '''
    
    if sum_E > sum_L:
        return 'emart'
    else:
        return 'lotte_mart'
#최저가 계산 //a안에 들어있는 true 값들을 계속 비교하여 같은 것만, 총 가격 합산
def min_value_E(a,b,c):
    sum_E=0
    for x in range(len(a)):
        if str(a[x]) ==c:
            sum_E += int(b[0].price)
    return sum_E
            
def min_value_L(a,b,c):
    sum_L=0
    for x in range(len(a)):
        if str(a[x]) ==c:
            sum_L += int(b[0].price)
    return sum_L
    
            
#자취생 지수 구하는 함수
def factor(request):
    re = Rice_E.objects.all()
    we = Water_E.objects.all()
    te = Tissue_E.objects.all()
    rl = Rice_L.objects.all()
    wl = Water_L.objects.all()
    tl = Tissue_L.objects.all()

    rice_factor_E =factoring(re)
    water_factor_E =factoring(we)
    tissue_factor_E =factoring(te)
    rice_factor_L =factoring(rl)
    water_factor_L =factoring(wl)
    tissue_factor_L =factoring(tl)

    # 각 이마트의 자취생 지수 구하기 가중치는 임의로 선정 (ex)쌀 40, 물 40 휴지 20)
    emart_factors = ((rice_factor_E *40) + (water_factor_E *40) + (tissue_factor_E*20)) / 100
    lotte_factors = ((rice_factor_L *40) + (water_factor_L *40) + (tissue_factor_L*20)) / 100
    
   # 오늘의 자취생 지수는 가중치 없이 평균으로 계산
    today_factors = (emart_factors+lotte_factors)/2

    #자취생 지수를 그래프로 보여주기
    y = [100,120,120,115,100]  # fake 데이터
    y.append(today_factors)
    
    x = np.arange(len(y))
    plt.plot(y)
    xlabel = ['7/27', '7/28', '7/29', '7/30', '7/31', '8/1']
    plt.xticks(x, xlabel)
    
    plt.savefig('C:/Users/sec/Desktop/github/Django/askdjango/blog/static/img/test.png')
    


    return render(request, 'blog/factor.html', {'emart_factors':emart_factors, 
                                                'lotte_factors':lotte_factors, 'today_factors':today_factors })

# 마트별 각 품목의 지수 구하는 함수
def factoring(a):
    sum = 0
    for x in range(len(a)):
        sum += int(a[x].price)
        average = sum/len(a)
        factor = ((average+10000)/average)*100   # 일단 전날 대비 평균가 만원 올랐다 가정
    return factor


# 게시판 함수
rowsPerPage = 3
view_number= 3  # 게시판에 보여지는 글 목록의 숫자
def board(request):
    boards=Board.objects.all().order_by('-id')[0:view_number]
    current_page=1
    totalCnt =Board.objects.all().count()

    pagingHelperIns = pagingHelper()
    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)

    content={'current_page': current_page, 'totalCnt': totalCnt, 'boards': boards,'totalPageList':totalPageList }
    return render(request, 'blog/board.html',content)
#게시판 목록넘기기 [1],[2],[3]..함수
def listPageWork(request):
    page= request.GET['current_page']
    current_page = page
    a=view_number*int(page) # 게시물의 총 개수 // str , int 조심
    b= (a-3)
    boards=Board.objects.all().order_by('-id')[b:a] # 보여주는 게시물 수를 3개로 계속 조절
    totalCnt =Board.objects.all().count()
    pagingHelperIns = pagingHelper()
    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)

    content={'current_page': current_page, 'totalCnt': totalCnt, 'boards': boards,'totalPageList':totalPageList }
    return render(request, 'blog/board.html',content)


#paging class 보여주는 페이지 조절하는 함수를 담은 클래스
class pagingHelper:
    
    def getTotalPageList(self, total_cnt, rowPerPage):
        if ((total_cnt % rowsPerPage)==0):
            self.total_pages =total_cnt /rowsPerPage
        else:
            self.total_pages =(total_cnt /rowsPerPage)+1
        
        self.totalPageList=[]
        for j in range(int(self.total_pages)):
            self.totalPageList.append(j+1)
        return self.totalPageList

    def __init__(self):
        self.total_pages=0
        self.totalPageList=0    

#게시판 글쓰기 함수
def board_writing_form (request):
     if request.method =='POST':
        form=BoardForm(request.POST)
        if form.is_valid():
            board =Board()
            board.subject = form.cleaned_data['subject']
            board.name = form.cleaned_data['name']
            board.memo = form.cleaned_data['memo']
            now =datetime.today().strftime('%Y-%m-%d')  # 모델 의 형식에 맞춰서 넣어야 한다.
            board.created_date =now #입력시간 자동 입력
            board.save()
        else:
            form.errors
        return redirect('/blog/board/')
     else:
        form =BoardForm()
     return render(request, 'blog/board_writing_form.html' ,{'form': form},)    
#게시판 글보기
def viewboard(request):
    pk= request.GET['memo_id']
    boardData = Board.objects.get(id=pk)
    Board.objects.filter(id=pk).update(hits = int(boardData.hits) + 1) #조회수 늘리기
    form =BoardForm()
    
    return render(request, 'blog/viewboard.html', {'memo_id': request.GET['memo_id'],
                                                'current_page':request.GET['current_page'],
                                                'searchStr': request.GET['searchStr'],
                                                'boardData': boardData, 'form': form } )
#게시판 검색결과 보여주기 함수
def  searchWithSubject(request):
    if 'searchStr' in request.GET and request.GET['searchStr']:
        searchStr = request.GET['searchStr']
        boards=Board.objects.filter(Q(subject__icontains=searchStr) | Q(name__icontains=searchStr ) |Q(memo__icontains=searchStr))
        totalCnt =boards.count()
        boards=boards.order_by('-id')[0:view_number] #[0:3]
        current_page=1
        pagingHelperIns = pagingHelper()
        totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)

        content = {'current_page': current_page, 'totalCnt': totalCnt, 'boards': boards,'totalPageList':totalPageList,'query': searchStr }
    else: 
          return HttpResponse('Please submit a search term.')
        
    return render(request, 'blog/searchWithSubject.html',content)

# 검색결과페이지에서 [1],[2],[3] 넘기기 함수
def listPageWork1(request):
    page= request.GET['current_page']
    searchStr= request.GET['searchStr']
    current_page = page
    a=view_number*int(page) # 게시물의 총 개수 // str , int 조심
    b= (a-3)
    boards=Board.objects.filter(Q(subject__icontains=searchStr) | Q(name__icontains=searchStr ) | Q(memo__icontains=searchStr))
    totalCnt =boards.count()
    boards=boards.order_by('-id')[b:a]
    
    pagingHelperIns = pagingHelper()
    totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
    

    content={'current_page': current_page, 'totalCnt': totalCnt, 'boards': boards,'totalPageList':totalPageList ,'query': searchStr } #query리를 보내주는 것
    return render(request, 'blog/searchWithSubject.html',content)

    
    
    




         
        











