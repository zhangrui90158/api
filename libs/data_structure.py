from interface_framework.config.conf import *
from OpenSSL import crypto
import base64
import json
import uuid

class DataStructure():
    def __init__(self,headers,body):
        self.__headers = headers
        self.__body = body

    @property
    def headers(self):
        self.__headers = {"R-Merchant": "CNZHRUIDEV"}
        self.__headers["R-Signature"] = DataStructure.get_sign(self.body)
        return self.__headers

    @property
    def body(self):
        if not self.__body["journalNumber"]:
            self.__body["journalNumber"] = DataStructure.get_journalNumber()
        elif not self.__body["transTime"]:
            self.__body["transTime"] = str(int(time.time() * 1000))
        elif not self.__body["endpointIp"]:
            self.__body["endpointIp"] = "192.168.1.153"
        return self.__body

    @staticmethod
    def get_sign(res_body):
        """
        :parmas: 读取本地pfx文件，使用私钥进行'sha256'签名
        :return: base64签名
        """
        with open(pfx_file, 'rb') as f:
            p12 = crypto.load_pkcs12(f.read(), b"123456")
            sign = crypto.sign(p12.get_privatekey(), json.dumps(res_body).encode("utf-8"), "SHA256")
            b64_sign = str(base64.b64encode(sign))[2:-1]
            return b64_sign

    @staticmethod
    def get_journalNumber():
        uid = uuid.uuid4()
        jNumber = str(base64.b64encode(uid.bytes), encoding="utf-8")
        return jNumber

if __name__ == '__main__':
    header = {}
    body = {
        "version": "1.0",
		"transCode": "100001",
		"param": {
			"bizType": "CL"
		}
	}
    data = DataStructure(header,body)
    print(data.body)
    print(data.headers)
