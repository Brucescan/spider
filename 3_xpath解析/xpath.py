import requests
from lxml import etree

url = "https://www.baidu.com"
headers={
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':
    'gzip, deflate, br, zstd',
    'Accept-Language':
    'en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control':
    'max-age=0',
    'Connection':
    'keep-alive',

    'Host':
    'www.baidu.com',
    'Sec-Ch-Ua':
    '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'Sec-Ch-Ua-Mobile':
    '?0',
    'Sec-Ch-Ua-Platform':
    "Windows",
    'Sec-Fetch-Dest':
    'document',
    'Sec-Fetch-Mode':
    'navigate',
    'Sec-Fetch-Site':
    'none',
    'Sec-Fetch-User':
    '?1',
    'Upgrade-Insecure-Requests':
    '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}
resp = requests.get(url,headers=headers)

# if resp.status_code == 200:
#     print(resp.text)
# else:
#     pass

html = resp.text
# 第一种方式 实例化 建议使用
tree = etree.HTML(html)
# print(tree)

# xpath语法 按照路径的方式去查找
# 查找退出登录 当前是从根目录html下一层一层往下找
# /html/body/div/div/div/a/text() 按照路径一层一层往下找，把符合路径的数据都拿到
# text()获取路径下的字符串（文本）
# a_list = tree.xpath('/html/body/div/div/div/a/text()')

# 将节点对象转换为字符串
# a_list = tree.xpath('/html/body/div/div/div/a')
# for i in a_list:
    # 通过循环获取到了每一个i节点对象,都可以链式调用
    # 获取节点里面的文本
    # print(i.xpath('./text()'))
    # print(type(etree.tostring(i, encoding='utf-8').decode('utf-8')))#报错，因为text不需要使用tostring，已经是str类型了



# 假如我想要百度热搜，会发现里面嵌套了很多东西，所以我们需要另一种方式来提取数据
# //不参照当前的位置
# 获取当前tree对象里的所有a，无论a在哪
# a_list = tree.xpath('//span')
# 获取所有超链接里面的文本
# a_list = tree.xpath('//span/text()')
# print(a_list)
# 不管哪一种方式，好像都没那么完善


# 组合使用，也就是/和//组合使用
# div_list = tree.xpath('//a/span//text()')
# print(div_list)
# print('over!')

# 带条件的查找
# a_list = tree.xpath('//li//a/span/text()')
# print(a_list)

# 加条件
# a_list = tree.xpath('//a/span[@class="title-content-title"]')
# print(a_list[0].xpath('.//text()')) # .// 当前节点的无论子子孙孙（无论当前节点下的任何位置）  ./接着当前节点向下一个节点进行匹配，就是儿子节点

# a_list = tree.xpath('//a[1]/span[@class="title-content-title"]//text()')
# xpath从第一个开始，从第零个取会报错
# a_list = tree.xpath('//a[last()]/span[@class="title-content-title"]//text()')
# 获取最后一个，可以做加减，last()-1是倒数第二个，
# a_list = tree.xpath('//a[position()<3]/span[@class="title-content-title"]//text()')
# 获取前两个，一般不用
# a_list = tree.xpath('//a/span[@class="title-content-title"]//text()')[0]
# 其实都可以通过切片的方式进行截取数据
# print(a_list)
# 语法非常的简单好用

# 路径下的标签只要有属性都可以加条件（记得加@），使查找更精确


# 上面的都是获取文本内容，现在我们开始获取标签的属性
# 查找所有图片的src    @属性名
# print(tree.xpath('//img/@src'))
# 获取所有超链接
# print(tree.xpath('//a/@href'))

# 了解内容
# 查找div 条件是div标签class属性值为article
# print(tree.xpath('//div[@class="article"]'))
# 查找div 条件是div标签具有class属性
# print(tree.xpath('//div[@class]'))

# 多个条件
# 查找div标签class属性值为article并且id属性值为1
# print(tree.xpath('//div[@class="article" and @id="1"]'))

# 还有一种或
# 查找div标签class属性值为article或id属性值为1,也可以吧or写成|也行
# print(tree.xpath('//div[@class="article" or @id="1"]'))


resp.close()

