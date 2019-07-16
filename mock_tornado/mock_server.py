import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import define,options
import torndb_for_python3
import redis
from interface_framework.mock_tornado.handlers.urls import handlers
from interface_framework.mock_tornado.config import *

define("port",default= 9000,type= int,help="define default port")

class Application(tornado.web.Application):
    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        self.mydb = torndb_for_python3.Connection(**mysql_options)
        self.myredis = redis.StrictRedis(**redis_options)

def main():
    tornado.options.parse_command_line()
    app = Application(
        handlers,
        **setting,
    )
    # app.listen(9000)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()