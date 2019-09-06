
from selenium import  webdriver 
import time

driver = webdriver.Chrome() 

driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') # 访问页面
time.sleep(2)

comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') # 使用class_name找到评论
btn = driver.find_element_by_class_name('comment__show_all').find_element_by_class_name('js_get_more_hot')
time.sleep(1)
btn.click()
time.sleep(1)
print(len(comments)) # 打印获取到的评论个数
for comment in comments: # 循环
    sweet = comment.find_element_by_tag_name('p') # 找到评论
    print ('评论：%s\n ---\n'%sweet.text) # 打印评论

time.sleep(1)
driver.close() # 关闭浏览器