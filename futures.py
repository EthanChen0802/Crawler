from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup


def crawl(date):
    r = requests.get(
        'https://www.taifex.com.tw/cht/3/futContractsDate?queryDate={}%2F{}%2F{}'.format(date.year, date.month,
                                                                                         date.day))
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')


# 從今天開始找，每次往前一天
terminate = datetime.today() - timedelta(days=6)
search_date = datetime.today()
while True:
    search_date = search_date - timedelta(days=1)
    if search_date < terminate:
        break
    crawl(search_date)
