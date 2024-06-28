import requests
import os.path
import time
from lxml import etree

'''
重点是对他们共同的功能进行封装，也就是写个函数
可以看到三个案例都会使用到请求，只不过请求的url不同而已
所以我们可以使用url作为参数
'''


# 通过传递url，返回对应的xpath的tree对象
def get_html(url):
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 '
            'Safari/537.36 '
    }
    resp = requests.get(url, headers=headers)
    tree = etree.HTML(resp.content.decode())
    resp.close()
    return tree


# 起始url
url = 'https://www.shicimingju.com/bookmark/sidamingzhu.html'


# print(get_html(url))


# 获取书的内容与超链接
def get_book_con(tree):
    a_list = tree.xpath('//div[@class="book-item"]/h3/a')
    book_item = {}
    # print(a_list)
    for a in a_list:
        # 获取书名
        book_name = a.xpath('./text()')[0]
        # 拼接完整的超链接
        book_url = 'https://www.shicimingju.com' + a.xpath('./@href')[0]
        book_item[book_name] = book_url
    return book_item
    # 返回的应该是这种格式：{"三国演义"：https://www.shicimingju.com/book/sanguoyanyi.html}


# print(resp.content.decode())


def get_book_mulu(tree):
    li_list = tree.xpath('//div[@class="book-mulu"]/ul/li')
    book_mulu = {}
    for li in li_list:
        book_mulu_name = li.xpath('./a/text()')[0]
        book_mulu_url = 'https://www.shicimingju.com' + li.xpath('./a/@href')[0]
        book_mulu[book_mulu_name] = book_mulu_url
    return book_mulu
    # 返回与上面类似


def get_book_text(book_name, mulu_name, tree):
    # 获取章节内容并下载
    # 拼接书名和章节名称
    if not os.path.exists(book_name):
        os.makedirs(book_name)
    path = os.path.join(book_name, mulu_name + '.txt')

    text = ''.join(tree.xpath('//p/text()'))
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(book_name, mulu_name, 'over!')


# 循环获取四大名著的书名和url
for book_name, book_url in get_book_con(get_html(url)).items():
    # print(book_name)
    # 循环获取四大名著的章节名称和url
    for mulu_name, mulu_url in get_book_mulu(get_html(book_url)).items():
        # print(mulu_name)
        get_book_text(book_name, mulu_name, get_html(mulu_url))
        # 获取四大名著的章节内容
        time.sleep(1)

    # print(book_name, book_url)

'''
需求：
三国演义/
    第一回。。。。。。
    第二回。。。。。。
水浒传/
    第一回。。。。
    第二回。。。。
'''
