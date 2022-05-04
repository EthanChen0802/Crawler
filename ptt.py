import requests
from bs4 import BeautifulSoup

# request 請求網址
r = requests.get('http://disp.cc/b/PttHot')

# BeautifulSoup解析
soup = BeautifulSoup(r.text, 'html.parser')

# spans = soup.find_all('span', class_="L34")
#
# for span in spans:
#     a_tag = span.find('a')
#     if a_tag is not None:
#         url = 'http://disp.cc/b/' + a_tag.get('href')
#         print(span.get_text())
#         print(url)


spans = soup.select('span.L34')
for span in spans:
    a_tag = span.find('a')
    if a_tag is not None:
        url = 'http://disp.cc/b/' + a_tag.get('href')
        print(span.get_text())
        print(url)
