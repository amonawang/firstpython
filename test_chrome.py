from selenium import webdriver
import time
dr = webdriver.Firefox()
dr = webdriver.Chrome()
dr.get('http://www.baidu.com') #
print(dr.find_element_by_id("kw").text)
ele = dr.find_element_by_id("kw")
ele.send_keys("good")
eleSub = dr.find_element_by_id("su")
eleSub.click()
time.sleep(10)
print('Browser will be closed')


dr.quit() # dr.close()
print('Browser is close')


