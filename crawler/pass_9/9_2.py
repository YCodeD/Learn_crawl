from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

pagesource = driver.page_source
print(type(pagesource))
print(pagesource)
driver.close()