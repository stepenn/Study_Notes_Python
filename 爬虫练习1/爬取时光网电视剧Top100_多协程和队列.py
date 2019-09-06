from gevent import monkey
monkey.patch_all()
import gevent,requests,bs4,csv
from gevent.queue import Queue

w_file = open('D:\\time_movie.csv','w',newline = '',encoding='utf-8')
write= csv.writer(w_file) 
row_header = ['剧名','简介']
write.writerow(row_header)

work = Queue()

for x in range(10):
    if x == 0:
        x = ''
        url = 'http://www.mtime.com/top/tv/top100'
    else:
        url = 'http://www.mtime.com/top/tv/top100/index-'+str(x+1)+'.html'
    work.put_nowait(url)

def crawler():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url)
        bs = bs4.BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ul', id="asyncRatingRegion")
        for key in bs.find_all('li'):
            title = key.find('h2',class_="px14 pb6").text
            if key.find('p',class_="mt3") != None:
                info = key.find('p',class_="mt3").text
            write.writerow([title,info])

tasks_list  = [ ]

for x in range(2):
    task = gevent.spawn(crawler)
    tasks_list.append(task)

gevent.joinall(tasks_list)


