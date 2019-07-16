import logging
import os
import time


prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
today = time.strftime('%Y%m%d',time.localtime())
now = time.strftime('%Y%m%d_%H%M%S',time.localtime())


#JSON测试数据、LOG文件、report文件、执行用例用例路径
data_path = os.path.join(prj_path,"data")
log_file = os.path.join(prj_path,"log","log.txt")
# report_file = os.path.join(prj_path,"report","report1.html")
report_file = os.path.join(prj_path, 'report','report_{}.html'.format(now))  # 也可以每次生成新的报告
test_case_path = os.path.join(prj_path,"test\case")
file_path = os.path.join(prj_path,"debug","test.png")

#log配置
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=log_file,
    filemode="a"
)

# 数据库配置
db_host = '192.168.1.152'
db_port = 3306
db_user = 'root'
db_passwd = '123456'
db = 'test'


#是否发送邮件配置
send_email_label= False
# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = 'yiqiniutest@163.com'
smtp_password = 'a12345678'

sender = 'yiqiniutest@163.com'  # 发件人
receiver = 'zhangrui@yiqiniu.com'  # 收件人
# receiver = ('zhangrui@yiqiniu.com',"382944288@qq.com")
subject = '接口测试报告'  # 邮件主题

if __name__ == '__main__':
    logging.info(data_path)
    logging.info(test_case_path)