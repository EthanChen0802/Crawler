import requests
from bs4 import BeautifulSoup

r = requests.get('https://tw.stock.yahoo.com/quote/2409')

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    result_set = soup.find_all("ul")[16].select('li')

    for i in result_set:
        column = i.find_all('span')
        title = column[0].text
        content = column[1].text
        print(f'{title}: {content}')
