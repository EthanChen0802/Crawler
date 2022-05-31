from bs4 import BeautifulSoup
import requests
import pprint
import re

r = requests.get('https://airtw.epa.gov.tw/json/camera_ddl_pic/camera_ddl_pic_2022053114.json?t=1653980867521')

data = r.json()

result = []
for d in data:
    name = d['Name']

    try:
        pattern = re.search(r'(.+)\((AQI=(\d+))', name)
        print(pattern.group(1), pattern.group(2))
    except AttributeError:
        print(f'{name}: 沒有AQI資料')
