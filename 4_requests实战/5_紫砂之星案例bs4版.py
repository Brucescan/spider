import requests
from bs4 import BeautifulSoup

url = 'http://zishazx.com/product'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

params = {

}

resp = requests.get(url, headers=headers)

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
resp.close()
