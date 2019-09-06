##爬取5页,循环5次,将关键字"w"换成其它歌手的名字，一样可以爬取歌单

import requests,openpyxl
# 引用requests模块
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
# 伪装请求头

wb=openpyxl.Workbook()  
#创建工作薄
sheet=wb.active 
#获取工作薄的活动表
sheet.title='restaurants' 
#工作表重命名

sheet['A1'] ='歌曲名'     #加表头，给A1单元格赋值
sheet['B1'] ='所属专辑'   #加表头，给B1单元格赋值
sheet['C1'] ='播放时长'   #加表头，给C1单元格赋值
sheet['D1'] ='播放链接'   #加表头，给D1单元格赋值

for x in range(5):
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.song_next',
    'searchid':'64405487069162918',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(x+1),
    'n':'20',
    'w':'周杰伦',
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'    
    }
    # 将参数封装为字典
    res_music = requests.get(url,headers=headers,params=params)
    # 调用get方法，下载这个字典
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
    # list_music是一个列表，music是它里面的元素
        name = music['name']
        # 以name为键，查找歌曲名，把歌曲名赋值给name
        album = music['album']['name']
        # 查找专辑名，把专辑名赋给album
        time = music['interval']
        # 查找播放时长，把时长赋值给time
        link = 'https://y.qq.com/n/yqq/song/' + str(music['file']['media_mid']) + '.html\n\n'
        # 查找播放链接，把链接赋值给link
        sheet.append([name,album,time,link])
        # 把name、album、time和link写成列表，用append函数多行写入Excel
        print('歌曲名：' + name + '\n' + '所属专辑:' + album +'\n' + '播放时长:' + str(time) + '\n' + '播放链接:'+ url)

wb.save(r'D:\jay.xlsx')            
#最后保存并命名这个Excel文件