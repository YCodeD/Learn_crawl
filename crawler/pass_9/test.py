from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php')
time.sleep(2)

username = driver.find_element_by_id('user_login')
username.send_keys('spiderman')
password = driver.find_element_by_id('user_pass')
password.send_keys('crawler334566')
bt_login = driver.find_element_by_id('wp-submit')
bt_login.click()
time.sleep(2)

article = driver.find_element_by_partial_link_text('三')
article.click()
time.sleep(1)

comment = driver.find_element_by_tag_name('textarea')
comment.send_keys('20170717pm selenium')
submit = driver.find_element_by_id('submit')
submit.click()

driver.close()