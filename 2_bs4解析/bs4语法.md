切记不要文件名与第三方模块相同

    from bs4 import Beautifulsoup
    soup = Beautifulsoup(html_doc,'lxml')
    #html进行美化  
    print(soup.prettify())

