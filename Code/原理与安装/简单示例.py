from selenium import webdriver

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
driver = webdriver.Chrome(r'E:\Selenium\chromedriver.exe')

# 调用 WebDriver 对象的get方法 可以让浏览器打开指定网址
driver.get('https://www.baidu.com')

# 关闭浏览器窗口
driver.quit()