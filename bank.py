import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('http://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx')

data = []
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, "html.parser")
    tables = soup.find_all('table', attrs={'cellpadding': '2'})

    for table in tables:
        trs = table.find_all('tr')
        for tr in trs:
            date, price, value = [td.text for td in tr.find_all('td')]
            if date == '日期':
                continue
            data.append([date, price, value])

# pandas資料轉換
df = pd.DataFrame(data, columns=['日期', '買賣超金額', '台指期'])

# pandas匯出檔案
df.to_csv('big_eight.csv', encoding='utf_8_sig')
df.to_excel('big_eight.xlsx')
df.to_html('big_eight.html')
