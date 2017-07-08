#이마트에서 쌀 이름과 가격 크롤링 
import requests
from bs4 import BeautifulSoup
import pymysql.cursors
import MySQLdb
 
conn= MySQLdb.connect("localhost","root","0000","practicedb",charset='utf8' )
 
curs = conn.cursor()

#sql1 = """insert into blog_emart(price) values (%s)"""

req = requests.get('http://www.ssg.com/search.ssg?target=all&query=%EC%8C%80')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
#my_titles = soup.select('span.subject')
#my_prices = soup.select('span.applied .ssg_price')

one=[]
two=[]
none=[]


for title in soup.select('span.subject'):
     one.append(title.text)

     #print(title.text)
   

for price in soup.select('span.applied .ssg_price'):
     two.append(price.text)
     #print(price.text)


#curs.executemany("""insert into blog_emart(title, price) values (?, ?)""" ,(one, two) )  

sql = """insert into blog_emart(title,price) values (%s, %s) """ 



for x in range(len(one)):
  curs.execute(sql, (one[x], two[x])) 

conn.commit()
conn.close()

# 1분마다 주기적으로 받아오기
'''
import time
import logging
import requests
from bs4 import BeautifulSoup

def parse():
     req = requests.get('http://www.ssg.com/search.ssg?target=all&query=%EC%8C%80')
     html = req.text
     soup = BeautifulSoup(html, 'html.parser')
     for title in soup.select('span.subject'):
     print(price.text)
     print("------------------------------")

while True:
    logging.info('start parsing')
    parse()
    logging.info('parsing ends')
    logging.info('sleep in 60s')
    time.sleep(60)
'''