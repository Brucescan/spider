from selenium import webdriver
from selenium.webdriver.common.by import By

'''
一点都不推荐！！！
很简单，没有技术含量，只能作为辅助工具
'''
driver = webdriver.Chrome()
# 请求百度
driver.get('http://www.baidu.com')
# 返回截图
# driver.save_screenshot('baidu.png')

# 搜索关键字‘独揽第’
# driver.find_element(By.ID, 'kw').send_keys('独揽第')

# 点击id为su的搜索按钮
# driver.find_element(By.ID, 'su').click()

# 查看数据
print(driver.page_source)

# 得到cookie
# driver.get_cookie()

# 得到当前的url
# driver.current_url()

# 退出当前页面
# driver.close()

# 退出浏览器
# driver.quit()


