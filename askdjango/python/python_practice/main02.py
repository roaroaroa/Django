import requests
from bs4 import BeautifulSoup

req = requests.get('https://beomi.github.io/archive/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'h2'
    )
# my_titles는 list 객체
for title in my_titles:
    # Tag안의 텍스트
    print(title.text)