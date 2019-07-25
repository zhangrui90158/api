import logging
import os
import time

"""项目主路径、格式化时间年月日_时分秒"""
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
today = time.strftime('%Y%m%d',time.localtime())
now = time.strftime('%Y%m%d_%H%M%S',time.localtime())


#JSON测试数据、LOG文件、report文件、执行用例用例路径
data_path = os.path.join(prj_path,"data")
log_file = os.path.join(prj_path,"log","log.txt")
# report_file = os.path.join(prj_path,"report","report1.html")
report_file = os.path.join(prj_path, 'report','report_{}.html'.format(now))  # 也可以每次生成新的报告
test_case_path = os.path.join(prj_path,"test","case")
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
db_host = '192.168.1.1'
db_port = 3306
db_user = 'root'
db_passwd = '11111'
db = 'test'


"""mysql服务器配置"""
mysql_options = {
	"host": "192.168.1.16",
    "port":3306,
    "user": "root",
	"password": "123456",
	"database": "itcast",
    "charset":"utf8"
}


"""redis服务器配置"""
redis_options = {
    "host" :"192.168.1.16",
    "port" : 6379
}

#是否发送邮件配置
send_email_label= False
# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = 'test@163.com'
smtp_password = '111111'

sender = '123123@163.com'  # 发件人
receiver = '123123@163.com'  # 收件人
# receiver = ("',"")
subject = '接口测试报告'  # 邮件主题

if __name__ == '__main__':
    logging.info(data_path)
    logging.info(test_case_path)