import requests
from bs4 import BeautifulSoup
import time

url = 'http://zishazx.com/product'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

params = {
    'page': '1',
    'size_id': '1',
    'volum_id': '3',
    'price_id': '2',
    'category_id': '0',
    'prize_id': '1',
    'pug_id': '1',
}
# resp = requests.get(url, headers=headers, params=params)
# print(resp.content.decode())
for i in range(1, 5):
    params['page'] = str(i)
    resp = requests.get(url, headers=headers, params=params)

    # print(resp.text)
    soup = BeautifulSoup(resp.content.decode(), 'lxml')
    # 查找数据
    li_list = soup.find('ul', class_="list clearfix").find_all('li')

    # print(li_list)
    for li in li_list:
        # print(li.find('img')['src'])
        # 获取名称
        print(li.find('p', class_="name").string)
        print(li.find('p', class_="p_no").string)
    time.sleep(1)
    print("over!")
    resp.close()