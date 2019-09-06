# smtplib 用于邮件的发信动作
import smtplib
# 引入email包中构建文本内容的方法
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# 用于构建邮件头
from email.header import Header



# 发信方的信息：发信邮箱，QQ邮箱授权码
from_addr = '851385455@qq.com'
password = 'xahjqkjzzsicbbae'

# 收信方邮箱
to_addrs = ['mp.ok.happy@163.com','724515862@qq.com']

# 发信服务器
smtp_server = 'smtp.qq.com'

#邮件内容
text = '''你好！
​    我是soctt，很高兴认识你。
'''

msg = MIMEText(text,'plain','utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(",".join(to_addrs))
msg['Subject'] = Header('认识一下')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)

# 登录发信邮箱
server.login(from_addr, password)


# 发送邮件
server.sendmail(from_addr, to_addrs, msg.as_string())
# 关闭服务器
server.quit()



# 发信方的信息：发信邮箱，QQ 邮箱授权码
# from_addr = input('请输入登录邮箱：')
# password = input('请输入邮箱授权码：')

# 收信方邮箱
# to_addrs = []
# while True:
    # a=input('请输入收件人邮箱：')
    # to_addrs.append(a)
    # b=input('是否继续输入，n退出，任意键继续：')
    # if b == 'n':
        # break