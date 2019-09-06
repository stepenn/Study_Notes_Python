import requests,csv
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'

offset=0
#设置offset的起始值为0

csv_file=open(r'D:\articles.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)
list2=['标题','链接','摘要']
writer.writerow(list2)

while True:
    params={
        'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset':str(offset),
        'limit':'20',
        'sort_by':'voteups',
        }
    
    res=requests.get(url,headers=headers,params=params)
    
    articles=res.json()
    
    data=articles['data']
    
    for i in data:
        list1=[i['title'],i['url'],i['excerpt']]
        writer.writerow(list1)
    
    offset=offset+20
    
    if offset>40:
        break
    #如果offset大于40，即爬了两页，就停止
    #if articles['paging']['is_end'] == True:
    #如果键is_end所对应的值是True，就结束while循环。
        #break
csv_file.close()
print('okay')  