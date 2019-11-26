# 从selenium框架导入浏览器驱动
# 使用浏览器驱动控制浏览器
from selenium import webdriver
# 是让浏览器等待加载，避免加载不完全导致数据丢失
from selenium.webdriver.support.ui import WebDriverWait
# time.sleep() 让程序休眠
import time

import settings

# 此代码是面向对象思维的
class taobao_infos:
    # 对象初始化  __开头的方法叫魔术方法
    def __init__(self):
        # 让浏览器去指定的页面
        url = 'https://login.taobao.com/member/login.jhtml'

        self.url = url
        self.brower = webdriver.Chrome(executable_path='')