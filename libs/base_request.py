import json
from interface_framework.config.conf import *
import requests
from interface_framework.libs.data_structure import DataStructure
from interface_framework.libs.realpay import get_journalNumber,get_sign,get_refund,get_res_headers
import logging

class BaseCaseRequest():
    __instance = None

    def __new__(cls, *args, **kwargs):
        #单列模式实例
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,case_name):
        '''
        :param case_name: 根据用例名称实例化对象，初始化测试测数据
        参数与data.json里面的key 一一对应
        '''
        case_data = BaseCaseRequest.init_test_data(case_name)
        self.url = case_data.get('url')
        self.headers = case_data.get('headers')
        self.method = case_data.get('method')
        self.params = case_data.get('params')
        self.expect_res = case_data.get('expect_res')
        self.data_type = case_data.get('data_type')
        logging.info('url = {0}+ \n + params = {1} + \n + method = {2}'.format(self.url, self.params, self.method))
    
    @staticmethod
    def init_test_data(case_name):
        """
        :param case_name: 传入case的名称，
        :return: 返回request所需要的数据参数
        """
        with open(case_file, "rb") as f:
            case_data = json.load(f).get(case_name)
            return case_data

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
            if not self.headers and self.params:
                '''
                实例化请求数据结构、构造请求头、请求体
                请求header为空，调用实例中的添加签名、跟商户序列号
                对请求体进行加签、添加时间戳
                '''
                data_structure = DataStructure(self.headers, self.params)
                self.params = data_structure.body
                self.headers = data_structure.headers
                logging.info(self.params)
                logging.info(self.headers)
                res = requests.post(url= self.url, headers= self.headers, data = json.dumps(self.params)) # JSON格式请求
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
        #构造文件流返回
        with open(file_path, "rb") as f:
            return f


if __name__ == '__main__':
    data = BaseCaseRequest("test_payChannelCode_is_NULL")
    data.send_requests()





