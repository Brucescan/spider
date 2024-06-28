import re

# match和search函数一样，都是只匹配一次，
# 区别是search是包含就行，而match是必须从开头匹配，相当于多一个^号

# print(re.match('a','aAbc123'))

# print(re.match('x','aAbc123'))
# 很明显结果为none

# print(re.match('[ab]','aAbc123'))
# <re.Match object; span=(0, 1), match='a'>很明显结果为a

# print(re.match('[a-zA-Z0-9]{4}','aAb-c123'))
# 要求结果必须以数字或字母4位开头，很明显不是，所以匹配结果为none

# print(re.match('[a-zA-Z0-9]{2,}','abc123'))
# 结果为<re.Match object; span=(0, 6), match='abc123'>

print(re.match('[a-zA-Z0-9]{2,3}','abc123'))
# <re.Match object; span=(0, 3), match='abc'>



# 后面不想写了，理解就好



