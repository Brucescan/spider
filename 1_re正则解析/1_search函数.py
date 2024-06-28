import re

# search 函数 只匹配一次，包含就可以


# print(re.search('a','aAbc123'))
# 返回结果 <re.Match object; span=(0, 1), match='a'>

# print(re.search('a','aAbc123').group())
# 匹配成功后可使用.group()进行获取匹配结果,结果为a

# print(re.search('x','aAbc123'))
# 返回结果None,表示匹配失败

# print(re.search('[ab]','aAbc123'))
# 返回的是a或者b，就近原则，返回的是a，若b在前面，则返回的是b

# print(re.search('[a-zA-Z0-9]{4}','aAb-c123'))
# 返回结果是 <re.Match object; span=(4, 8), match='c123'>，匹配的时候是连续匹配的

# print(re.search('[a-zA-Z0-9]{2,}','abc123'))
# 返回结果是 <re.Match object; span=(0, 6), match='abc123'>

# print(re.search('[a-zA-Z0-9]{2,3}','abc123'))
# 返回结果<re.Match object; span=(0, 3), match='abc'> ，可以看到给出一个范围的限定符时，会尽可能多的匹配字符

# print(re.search('[a-zA-Z0-9]?','abc123'))
# 返回结果 <re.Match object; span=(0, 1), match='a'>

# print(re.search('[a-zA-Z]?','123'))
# 返回结果 <re.Match object; span=(0, 0), match=''>，匹配成功，但没有匹配结果，也可以使用{0,1}代替问好

# print(re.search('\d{0,1}','123'))
# print(re.search('\D{1}','123'))
# <re.Match object; span=(0, 1), match='1'>
# None 没有匹配

# print(re.search('\s','123\n'))
# 返回结果 <re.Match object; span=(3, 4), match='\n'>

# print(re.search('\S','123\n'))
# 返回结果 <re.Match object; span=(0, 1), match='1'>

print(re.search('^1[3-9][0-9]{9}','218739878035'))
# 返回结果时 <re.Match object; span=(1, 12), match='18739878035'>说明正则与字符串之间应该是包含关系，包含就成功
