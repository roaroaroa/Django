#이마트와 롯데마트에서 쌀/물/휴지 title과 price 클롤링하기
import requests
from bs4 import BeautifulSoup
import pymysql.cursors
import MySQLdb
 
conn= MySQLdb.connect("localhost","root","0000","practicedb",charset='utf8' )
 
curs = conn.cursor()
#이마트 쌀
req = requests.get('http://www.ssg.com/search.ssg?target=all&query=%EC%8C%80')
html = req.text
soup_rice_E = BeautifulSoup(html, 'html.parser')
#이마트 물
req = requests.get('http://www.ssg.com/search.ssg?target=all&query=%EB%AC%BC')
html = req.text
soup_water_E = BeautifulSoup(html, 'html.parser')
#이마트 휴지
req = requests.get('http://www.ssg.com/search.ssg?target=all&query=%ED%9C%B4%EC%A7%80')
html = req.text
soup_tissue_E = BeautifulSoup(html, 'html.parser')

#롯데마트 쌀
req = requests.get('http://www.lottemart.com/search/search.do?searchTerm=%EC%8C%80&viewType=&searchField=')
html = req.text
soup_rice_L = BeautifulSoup(html, 'html.parser')
#롯데마트 물
req = requests.get('http://www.lottemart.com/search/search.do?searchTerm=%EC%83%9D%EC%88%98&viewType=gallery&searchField=')
html = req.text
soup_water_L = BeautifulSoup(html, 'html.parser')
#롯데마트 휴지
req = requests.get('http://www.lottemart.com/search/search.do?searchTerm=%ED%9C%B4%EC%A7%80&viewType=gallery&searchField=')
html = req.text
soup_tissue_L = BeautifulSoup(html, 'html.parser')


#넣을 때 부터 정수화 시켜서 디비에 넣기
rice_emart=[]
rice_price_E=[]
water_emart=[]
water_price_E=[]
tissue_emart=[]
tissue_price_E=[]


rice_lotte=[]
rice_price_L=[]
water_lotte=[]
water_price_L=[]
tissue_lotte=[]
tissue_price_L=[]

def insert_title_E(a, b):
    for title in a.select('span.subject'):
        b.append(title.text.strip())

def insert_price_E(x, y):
    for price in x.select('span.applied .ssg_price'):
        a =price.text.replace(',', '')
        b =int(a)
        y.append(b)
def insert_title_L(a, b):
    for title in a.select('p.prod-name'):
        b.append(title.text.strip())

def insert_price_L(x, y):
    for price in x.select('span.num-n'):
        a =price.text.replace(',', '')
        b =int(a)
        y.append(b)

# 이마트
insert_title_E(soup_rice_E, rice_emart)
insert_price_E(soup_rice_E, rice_price_E)
insert_title_E(soup_water_E, water_emart)
insert_price_E(soup_water_E, water_price_E)
insert_title_E(soup_tissue_E, tissue_emart)
insert_price_E(soup_tissue_E, tissue_price_E)
# 롯데마트
insert_title_L(soup_rice_L, rice_lotte)
insert_price_L(soup_rice_L, rice_price_L)
insert_title_L(soup_water_L, water_lotte)
insert_price_L(soup_water_L, water_price_L)
insert_title_L(soup_tissue_L, tissue_lotte)
insert_price_L(soup_tissue_L, tissue_price_L)


sql_re = """insert into blog_rice_e(title,price) values (%s, %s) """
sql_we = """insert into blog_water_e(title,price) values (%s, %s) """ 
sql_te = """insert into blog_tissue_e(title,price) values (%s, %s) """ 

sql_rl = """insert into blog_rice_l(title,price) values (%s, %s) """ 
sql_wl = """insert into blog_water_l(title,price) values (%s, %s) """ 
sql_tl = """insert into blog_tissue_l(title,price) values (%s, %s) """ 

def mysql(a,b,c):
  for x in range(len(a)):
     curs.execute(c, (a[x], b[x])) 

#이마트
mysql(rice_emart, rice_price_E, sql_re)
mysql(water_emart, water_price_E, sql_we)
mysql(tissue_emart, tissue_price_E, sql_te)
#롯데마트
mysql(rice_lotte, rice_price_L, sql_rl)
mysql(water_lotte, water_price_E, sql_wl)
mysql(tissue_lotte, tissue_price_L, sql_tl)

conn.commit()
conn.close()

