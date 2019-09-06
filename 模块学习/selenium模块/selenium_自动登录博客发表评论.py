from selenium import  webdriver 
import time
driver = webdriver.Chrome() 
url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'

driver.get(url) 
time.sleep(2)

user = driver.find_element_by_id('user_login')
user.send_keys('spiderman')
password = driver.find_element_by_id('user_pass')
password.send_keys('crawler334566')
time.sleep(1)
button = driver.find_element_by_id('wp-submit')
time.sleep(1)
button.click()
link = driver.find_element_by_link_text('未来已来（三）——同九义何汝秀')
time.sleep(1)
link.click()
comment = driver.find_element_by_id('comment')




