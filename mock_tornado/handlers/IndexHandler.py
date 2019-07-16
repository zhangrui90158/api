from .BaseHandler import BaseHandler
from interface_framework.config.conf import *
import json
class IndexHandler(BaseHandler):
    """
    接收请求方法，响应数据，获取JSON格式数据后返回
    """
    def prepare(self):
        """预解析json数据"""
        if self.request.headers.get("Content-Type").startswith("application/json"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict = None

    def post(self):
        if self.json_dict:
            self.write(self.json_dict)
            # for key, value in self.json_dict.items():
            #     self.write("<h3>{0}</h3><p>{1}</p>".format(key,value))
    def get(self):

        err_code = self.get_argument("code", None)  # 注意返回的是unicode字符串，下同
        err_title = self.get_argument("title", "")
        err_content = self.get_argument("content", "")
        if err_code:
            self.send_error(int(err_code), title=err_title, content=err_content)
        else:
            self.write("主页")

    def write_error(self, status_code: int, **kwargs):
        self.write(u"<h1>出错了，程序员GG正在赶过来！</h1>")
        self.write(u"<p>错误名：%s</p>" % kwargs["title"])
        self.write(u"<p>错误详情：%s</p>" % kwargs["content"])

class IndexJson(BaseHandler):

    def post(self):
        data = {
            "name": "zhangsan",
            "age": 24,
            "gender": 1,
        }
        json_data = json.dumps(data)
        self.write(json_data)


class ItcastHandler(BaseHandler):

    def initialize(self,subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)

class UploadHandler(BaseHandler):
    """获取上传文件"""
    def post(self):
        files = self.request.files.get("image")
        if files:
            image_file = files[0]["body"]
            with open("test.png","wb") as f:
                f.write(image_file)
        self.write("OK")

class SubjectCityHandler(BaseHandler):
    def get(self, subject, city):
        self.write(("Subject: %s<br/>City: %s" % (subject, city)))

class SubjectDateHandler(BaseHandler):
    def get(self, date, subject):
        self.write(("Date: %s<br/>Subject: %s" % (date, subject)))


class InsertHandler(BaseHandler):
    def post(self):
        """
        获取请求参数，插入数据库
        :return:
        """
        title = self.get_argument("title")
        position = self.get_argument("position")
        price = self.get_argument("price")
        score = self.get_argument("score")
        comments = self.get_argument("comments")
        logging.info(title)
        try:
            ret = self.application.mydb.execute("insert into houses(title, position, price, score, comments) values""(%s, %s, %s, %s, %s)",
                                                title, position, price, score, comments)
        except Exception as e:
            self.write("DB error:%s" % e)
        else:
            self.write("OK %d" % ret)
        self.write("数据写入成功")
