import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
from interface_framework.config.conf  import *

def send_email(report_file):
    msg = MIMEMultipart()#混合MIME模式
    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'html','utf-8')) # 添加html格式邮件正文（会丢失css格式）

    msg['From'] = 'yiqiniutest@163.com' #发件人
    msg['To'] = 'zhangrui@yiqiniu.com' #收件人
    msg['Subject'] = Header('接口测试报告','utf-8')

    # 3构造附件1，传送当前目录下的文件
    atth = MIMEText(open(report_file,'rb').read(),'base64','utf-8') # 二进制格式打开
    atth["Content-Type"] = 'application/octet-stream'
    atth["Content-Disposition"] = 'attachment; filename="report1.html"'  # filename为邮件中附件显示的名字
    msg.attach(atth)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server)# smtp服务器地址 使用SSL模式,从配置文件中读取
        smtp.login(smtp_user, smtp_password)  # 用户名和密码# 从配置文件中读取
        smtp.sendmail(sender, receiver, msg.as_string())
        # smtp.sendmail("test_results@sina.com", "superhin@126.com", msg.as_string())  # 发送给另一个邮箱
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

if __name__ == '__main__':
    # send_email(report_file)
    report_file = os.path.join(prj_path,"report","report1.html")
    send_email(report_file)