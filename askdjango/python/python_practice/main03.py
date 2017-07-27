#최저가 순으로 저장된 디비에서 최저가 3가지 추출(이마트와 롯데마트)// 쌀 //물//휴지//처리 할 수 있게 가격을 int화 까지
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
req = requests.get('http://www.lottemart.com/search/search.do?searchTerm=%EB%AC%BC&viewType=gallery&searchField=')
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

#이마트 쌀 이름
for title in soup_rice_E.select('span.subject'):
     rice_emart.append(title.text.strip())
#이마트 쌀가격
for price in soup_rice_E.select('span.applied .ssg_price'):
     a=price.text.replace(',','')
     b=int(a)
     rice_price_E.append(b)
#이마트 물 이름
for title in soup_water_E.select('span.subject'):
     water_emart.append(title.text.strip())
#이마트 물 가격
for price in soup_water_E.select('span.applied .ssg_price'):
     a=price.text.replace(',','')
     b=int(a)
     water_price_E.append(b)
#이마트 휴지 이름
for title in soup_tissue_E.select('span.subject'):
     tissue_emart.append(title.text.strip())
#이마트 휴지 가격
for price in soup_tissue_E.select('span.applied .ssg_price'):
     a=price.text.replace(',','')
     b=int(a)
     tissue_price_E.append(b)

#####
#롯데마트 쌀 이름
for title in soup_rice_L.select('p.prod-name'):
     rice_lotte.append(title.text.strip())
#롯데마트 쌀 가격
for price in soup_rice_L.select('span.num-n'):
     a=price.text.replace(',','')
     b=int(a)
     rice_price_L.append(b)
#롯데마트 물 이름
for title in soup_water_L.select('p.prod-name'):
     water_lotte.append(title.text.strip())
#이마트 물 가격
for price in soup_water_L.select('span.num-n'):
     a=price.text.replace(',','')
     b=int(a)
     water_price_L.append(b)
#롯데마트 휴지 이름
for title in soup_tissue_L.select('p.prod-name'):
     tissue_lotte.append(title.text.strip())
#롯데마트 휴지 가격
for price in soup_tissue_L.select('span.num-n'):
     a=price.text.replace(',','')
     b=int(a)
     tissue_price_L.append(b)
     




sql_E=""" insert into blog_handling2(title1, min_order1, title2, min_order2,title3,min_order3) values (%s,%s,%s,%s,%s,%s)"""  # %d로는 안됨
sql_L=""" insert into blog_handling3(title1, min_order1, title2, min_order2,title3,min_order3) values (%s,%s,%s,%s,%s,%s)""" 

for x in range(len(rice_emart)):    
    curs.execute(sql_E,(rice_emart[x],rice_price_E[x],water_emart[x],water_price_E[x],tissue_emart[x],tissue_price_E[x]))

for x in range(len(rice_lotte)):  
    curs.execute(sql_L,(rice_lotte[x],rice_price_L[x],water_lotte[x],water_price_L[x],tissue_lotte[x],tissue_price_L[x]))

conn.commit()
conn.close()
