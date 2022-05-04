import requests
import pprint
from bs4 import BeautifulSoup

r = requests.get("https://www.dcard.tw/f/job/p/238777200")

soup = BeautifulSoup(r.text, 'html.parser')

spans = soup.select('.sc-995d8868-1')

root_url = "https://www.dcard.tw"

#  字典
data = {}

for span in spans:
    title = span.find('span', class_="jia-DIw")
    content = span.find('a', class_='sc-5ebd82a8-1')

    if (title is not None) & (content is not None):
        # 清單
        comment_list = []

        # 帳號和留言網址
        account = title.text
        comment = root_url + content.get('href')

        if account in data:
            data.get(account).append(comment)
        else:
            comment_list.append(comment)
            data[account] = comment_list

pprint.pprint(data)

# 查找最多的留言學校
max_comment_count = 0
result = ""
for key in data:
    tmp_count = len(data[key])
    if tmp_count > max_comment_count:
        max_comment_count = tmp_count
        result = key

print(f"Most comments are from {result} which are {max_comment_count} in total")
