import csv

#读取文件
# r_file = open('d:/360MoveData/Users/Administrator/Desktop/Python_Study/模块学习/csv模块/test.csv','r',newline = '', encoding = 'utf-8')
# reader = csv.reader(r_file)
with open('d:/360MoveData/Users/Administrator/Desktop/Python_Study/模块学习/csv模块/test.csv', newline = '', encoding = 'utf-8')  as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)

#写入文件——————一行列表数据
# w_file = open('d:/360MoveData/Users/Administrator/Desktop/Python_Study/模块学习/csv模块/test.csv','w',newline = '', encoding = 'utf-8')
# writer = csv.writer(w_file)
with open('d:/360MoveData/Users/Administrator/Desktop/Python_Study/模块学习/csv模块/test.csv','a', newline='',encoding='utf-8') as f:
    writer  = csv.writer(f)
    writer.writerow(['8', '猫砂', '25', '1022', '886'])
    writer.writerow(['9', '猫罐头', '18', '2234', '3121'])