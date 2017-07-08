#이마트에서 가져온 쌀 데이터 중 최고가, 최저가 처리
import requests
from bs4 import BeautifulSoup
import pymysql.cursors
import MySQLdb
 
conn= MySQLdb.connect("localhost","root","0000","practicedb",charset='utf8' )
 
curs = conn.cursor()

req = requests.get('http://www.ssg.com/search.ssg?target=all&query=%EC%8C%80')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

one=[]
two=[]
int_two=[]

for title in soup.select('span.subject'):
     one.append(title.text)
     #print(title.text)
   

for price in soup.select('span.applied .ssg_price'):
     two.append(price.text)
     #print(price.text)


for i in range(len(two)):
    a=two[i].replace(',','')
    b=int(a)
    int_two.append(b)

min_value=min(int_two)
max_value=max(int_two)



for i in range(len(one)):
      if(int_two[i]==max_value):
         title=one[i]

for i in range(len(one)):
      if(int_two[i]==min_value):
         title1=one[i]
     



sql=""" insert into blog_handling(title, max_value, title1, min_value) values (%s,%s,%s,%s)"""  # %d로는 안됨


curs.execute(sql,(title,max_value,title1,min_value))
conn.commit()
conn.close()
