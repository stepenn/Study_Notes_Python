import requests
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
url_lyric = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg'

headers = {
    'origin':'https://y.qq.com',
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
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
    res_music = requests.get(url,headers=headers,params=params)
    json_music = res_music.json()
    list_music = json_music['data']['song']['list']
    id_all = []
    for music in list_music:
        id_all.append(music['id'])

    for lyric in id_all:
        params1 = {
            'nobase64':'1',
            'musicid':str(lyric),
            '-':'jsonp1',
            'g_tk':'708179507',
            'loginUin':'851385455',
            'hostUin':'0',
            'format':'json',
            'inCharset':'utf8',
            'outCharset':'utf-8',
            'notice':'0',
            'platform':'yqq.json',
            'needNewCode':'0'
        }
        res_lyric = requests.get(url_lyric,headers=headers,params=params1)
        json_lyric = res_lyric.text
        print(json_lyric)