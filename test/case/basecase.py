import os
import json
import unittest
from data_driver_interface_framework.config.conf import *
import requests

class BaseCaseRequest():
    __instance = None

    def __new__(cls, *params, **kwparams):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,case_name):
        self.case_name = case_name
        self.data_file = os.path.join(data_path, "data.json")
        with open(self.data_file, "rb") as f:
            self.case_data = json.load(f).get(case_name)

        self.url = self.case_data.get('url')
        self.headers = self.case_data.get('headers')
        self.method = self.case_data.get('method')
        self.params = self.case_data.get('params')
        self.expect_res = self.case_data.get('expect_res')
        self.data_type = self.case_data.get('data_type')
        logging.info('url = {0}+ \n + params = {1} + \n + method = {2}'.format(self.url, self.params, self.method))

    def send_requests(self):
        if self.url and self.method.upper() == "GET":
            if not self.params:
                res = requests.get(url= self.url, headers = self.headers)
                return res.json()
            else:
                res = requests.get(url= self.url, params= self.params,headers = self.headers)
                return res.json()

        elif self.method.upper() == "POST" and self.data_type.upper() == "APPLICATION/JSON":
            res = requests.post(url= self.url, json = json.loads(self.params), headers= json.loads(self.headers)) # JSON格式请求
            return res.json()

        elif self.method.upper() == "POST" and self.data_type.upper() == "FROM":
            res = requests.post(url= self.url, data= json.loads(self.params), headers= json.loads(self.headers))
            return res.text
        else:
            return

if __name__ == '__main__':
    data = BaseCaseRequest("baidu")
    data.send_requests()




