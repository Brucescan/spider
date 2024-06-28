xpath简单好用  
> html_tree = etree.parse('XX.html')  
> 
> 解析本地html文件
> 
> html_tree = etree.HTML(html字符串)
> 
> 推荐使用，解析网络的html字符串
> 
> html_tree.xpath()
> 
> 使用xpath路径查询信息，返回一个列表
> 
注意，如果解析本地HTML文件报错可以按照如下添加参数

    parser = etree.HTMLParser(encoding="utf-8")
    selector=etree.parse('./xx.html',parser=parser)
    result = etree.tostring(selector)
接下来直接上例子
