import requests, openpyxl, bs4

wb=openpyxl.Workbook()
sheet=wb.active 
sheet.title='movie' 

sheet['A1'] ='序号'     
sheet['B1'] ='电影名'  
sheet['C1'] ='评分'   
sheet['D1'] ='播放链接'
sheet['E1'] = '推荐语'

for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        num = titles.find('em',class_="").text
        #序号
        title = titles.find('span', class_="title").text
        #电影名
        comment = titles.find('span',class_="rating_num").text
        #评分
        url_movie = titles.find('a')['href']
        #链接
        if titles.find('span',class_="inq") != None:
            tes = titles.find('span',class_="inq").text
            #推荐语
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
        else:
            print(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie)
        
        sheet.append([num,title,comment,url_movie,tes])

wb.save(r'D:\movie.xlsx')  