import os

"""静态文件跟模板存放路径"""
setting = {
    "static_path" :os.path.join(os.path.dirname(__file__),"static"),
    "template_path": os.path.join(os.path.dirname(__file__),"template"),
    "cookie_secret":"S4aBKI5uT1OBRbRtqMJyCPmd1OmlHUeVvQWDuFK4axE=",
    "xsrf_cookies":False,
    "debug":True
}

"""mysql服务器配置"""
mysql_options = {
	"host": "192.168.1.16",
    "user": "root",
	"password": "123456",
	"database": "itcast"
}

"""redis服务器配置"""
redis_options = {
    "host" :"192.168.1.16",
    "port" : 6379
}