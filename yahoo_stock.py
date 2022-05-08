import pandas as pd
import requests
from bs4 import BeautifulSoup

r = requests.get('https://tw.stock.yahoo.com/quote/2409')

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    result_set = soup.find_all("ul")[16].select('li')

    title_list = []
    content_list = []

    for i in result_set:
        column = i.find_all('span')
        title = column[0].text
        content = column[1].text
        title_list.append(title)
        content_list.append(content)

    stock_name = soup.find('h1').text
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.width', 1000)
    df = pd.DataFrame(content_list, index=title_list, columns=[stock_name])
    print(df)
