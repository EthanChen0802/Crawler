from bs4 import BeautifulSoup
import requests

data = {'timestamp': '1598641153', 'Submit': 'Convert'}
r = requests.post('https://www.unixtimestamp.com/', data=data)

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    tables = soup.find_all('table')

trs = tables[2].find_all('tr')
tds = trs[4].find_all('td')
print(f'UnixTime轉換後的時間為: {tds[0].text}')
