from bs4 import BeautifulSoup

# 使用的第一种方式
# f = open('wenjian', 'r',encoding='UTF-8')这里我们没有文件，不做演示
# soup = BeautifulSoup(f.read(),'lxml')
# print(soup)

# 获取标签属性，两种
# 1、.方式进行获取
# 2、find方式进行获取

# 获取文本内容

# print(soup.find('div'))
# print(soup.find('div').string) #None
# print(soup.find('div').text)#获取所有文本
# print(soup.find('div').get_text())获取所有文本
# print(soup.find('div').strings)获取所有文本
# print(soup.find('div').stripped_strings) #获取所有文本并去除空白行


# 美化打印
# print(soup.find('div').prettify())


# 获取所有，findAll或者find_all,和find使用方法一样
# print(soup.find_all('a'))
# print(soup.find_all('img'))

# 添加条件
# print(soup.find_all('a',class_='title'))#注意class要加_，因为会与python内置的类冲突
# print(soup.find_all('a',attrs={'class':'title'}))
# 若是想找没有属性的标签可以往上进行查找即可

# print(soup.find_all('a',attrs={'class':'title'})[0].find_all('li'))
# 里面就一个bs4对象，所以可以继续链式调用,找没有属性的li标签，正常情况下写应该是这样的
# print(soup.find('a',attrs={'class':'title'}).find_all('li'))

# 一般用不到,不方便
# print(soup.find('a',attrs={'class':'title'}).find_all('li',limit=2))

# 选择器（用的少） 获取所有
# print(soup.select('img'))#填写标签即可
# print(soup.select('.cover'))类选择器选择属性值为cover的标签
# print(soup.select('#cover'))#id选择器，选择所有属性值为cover的标签
# print(soup.select('.cover#cover'))
# 也可以进行链式调用

# 代码不重要，重要的是拿到代码的思路，所以我就不往下写了


