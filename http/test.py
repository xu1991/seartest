from selenium import webdriver
import time


# !!!!注意这里的路径是PhantomJS存放的路径
# 这个是一个用来控制chrome以无界面模式打开# 的浏览器
# 创建一个参数对象，用来控制chrome以无界面的方式打开
# chrome_options = Options()
# # 后面的两个是固定写法 必须这么写
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# # 驱动路径 谷歌的驱动存放路径
# path = r'C:\Users\aisino\AppData\Local\Google\Chrome\Application\chromedriver.exe'
# # 创建浏览器对象
# browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
browser = webdriver.PhantomJS(r'/opt/app-root/src/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
url = r'https://www.google.com/webhp?hl=zh-CN&sa=X&ved=0ahUKEwjm_7ORv-jkAhWHfXAKHeEjA1YQPAgH'
browser.get(url)
time.sleep(3)
browser.save_screenshot('1.png')
browser.close()
