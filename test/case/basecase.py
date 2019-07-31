import json
from interface_framework.config.conf import *
import requests
from interface_framework.libs.realpay import get_journalNumber,get_sign,get_refund,get_res_headers
import logging

class BaseCaseRequest():
    __instance = None

    def __new__(cls, *args, **kwargs):
        '''
        :param params:可变参数
        :param kwparams:键值对参数
        :return: 单列实例
        '''
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,case_name):
        '''
        :param case_name: 根据用例名称实例化对象，初始化测试测数据
        参数与data.json里面的key 一一对应
        '''
        self.case_name = case_name
        self.data_file = os.path.join(data_path, "realpay_data.json")
        with open(self.data_file, "rb") as f:
            self.case_data = json.load(f).get(case_name)

        self.url = self.case_data.get('url')
        self.headers = self.case_data.get('headers')
        self.method = self.case_data.get('method')
        self.params = self.case_data.get('params')
        self.expect_res = self.case_data.get('expect_res')
        print(self.expect_res)
        self.data_type = self.case_data.get('data_type')
        logging.info('url = {0}+ \n + params = {1} + \n + method = {2}'.format(self.url, self.params, self.method))

    def send_requests(self):
        '''
        根据请求类型发送get、post请求
        FROM = application/x-www-form-urlencoded数据格式
        JSON = application/json
        XML = text/xml
        MULTIPART = multipart/form-data
        根据请求方法和请求数据传输类型判断发送请求
        :return: 响应res，方便在用例集种根据响应信息扩展断言
        '''
        if self.method.upper() == "GET":
            if not self.params:
                res = requests.get(url= self.url, headers= self.headers)
                return res
            else:
                res = requests.get(url= self.url, headers= self.headers,params= self.params)
                return res

        elif self.method.upper() == "POST" and self.data_type.upper() == "FORM":
            res = requests.post(url= self.url, headers= self.headers, data= self.params)
            return res

        elif self.method.upper() == "POST" and self.data_type.upper() == "JSON":
            if not self.headers:
                '''
                请求header为空，添加签名、跟商户序列号
                对请求体进行加签、添加时间戳
                '''
                self.params["journalNumber"] = get_journalNumber()
                self.params["transTime"] = str(int(time.time()*1000))
                self.headers = {"R-Merchant":"CNZHRUIDEV"}
                self.headers["R-Signature"] = get_sign(self.params)
                logging.info(self.params)
                logging.info(self.headers)
                res = requests.post(url= self.url, headers= self.headers, data = json.dumps(self.params)) # JSON格式请求
                return res
            elif not self.headers and not self.params:
                '''
                请求header为空，添加签名、跟商户序列号
                对请求体进行加签、添加时间戳
                对请求body参数进行封装
                '''
                self.params = get_refund()
                self.headers = get_res_headers(self.params)
                logging.info(self.params)
                logging.info(self.headers)
                res = requests.post(url= self.url, headers= self.headers, data= json.dumps(self.params))  # JSON格式请求
                return res
            else:
                res = requests.post(url=self.url, headers=self.headers, data=json.dumps(self.params))  # JSON格式请求
                return res

        elif self.method.upper() == "POST" and self.data_type.upper() == "XML":
            res = requests.post(url= self.url, headers= self.headers, data= self.params)
            return res

        elif self.method.upper() == "POST" and self.data_type.upper() == "MULTIPART":
            files = {"file":self.file_stream()}
            res = requests.post(url= self.url, data= self.params, headers= self.headers, files= files)
            return res

        else:
            return

    def file_stream(self):
        with open(file_path, "rb") as f:
            return f


if __name__ == '__main__':
    data = BaseCaseRequest("test_payChannelCode_is_NULL")
    data.send_requests()




