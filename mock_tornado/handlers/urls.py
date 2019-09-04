from tornado.web import url
from .IndexHandler import *

handlers = [
        (r"/", IndexHandler),
        (r"/pay_status", PayStatusHandler),
        (r"/pay_json", IndexPayJson),
        (r"/refund_json", IndexRefundJson),
        (r"/insert", InsertHandler),
        (r"/sub-city/(.+)/([a-z]+)", SubjectCityHandler),  # 无名方式，正则表达式匹配
        (r"/sub-date/(?P<subject>.+)/(?P<date>\d+)",SubjectDateHandler),  # 命名方式
        (r"/upload", UploadHandler),
        (r"/cpp", ItcastHandler, {"subject": "c++"}),
        url(r"/python", ItcastHandler, {"subject": "python"}, name="python_url")
]