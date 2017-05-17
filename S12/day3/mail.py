import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail():
    ret = True
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["caijinxu",'enzof2004@126.com'])
        msg['To'] = formataddr(["德芙",'2423214641@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.126.com", 25)
        server.login("enzof2004@126.com", "邮箱密码")
        server.sendmail('enzof2004@126.com', ['2423214641@qq.com',], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret
ret = mail()
if ret:
    print('发送成功')
else:
    print('发送失败')