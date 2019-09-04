from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    '''
    自定义BaseHandler基类
    '''
    @property
    def mydb(self):
        """作为RequestHandler对象的db属性"""
        return self.application.mydb

    @property
    def myredis(self):
        """作为RequestHandler对象的redis属性"""
        return self.application.myredis

    def prepare(self):
        """预解析json数据"""
        # if self.request.headers.get("Content-Type").startswith("application/json"):
        #     self.json_dict = json.loads(self.request.body)
        # else:
        #     return
        pass

    def write_error(self, status_code: int, **kwargs):
        pass

    def set_default_headers(self):
        """设置默认json格式"""
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def initialize(self):
        """此方法通常用来初始化参数（对象属性）"""
        pass


    def on_finish(self):
        pass


