import os

setting = {
    "static_path" :os.path.join(os.path.dirname(__file__),"static"),
    "template_path": os.path.join(os.path.dirname(__file__),"template"),
    "cookie_secret":"S4aBKI5uT1OBRbRtqMJyCPmd1OmlHUeVvQWDuFK4axE=",
    "xsrf_cookies":False,
    "debug":True
}


mysql_options = {
	"host": "192.168.1.1",
    "user": "root",
	"password": "1111s11",
	"database": "test"
}


redis_options = {
    "host" :"192.168.1.1",
    "port" : 6379
}