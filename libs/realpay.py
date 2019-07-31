import requests
import json
import random
import base64
import uuid
from OpenSSL import crypto
from interface_framework.libs.my_mysql import My_Pymysql
from interface_framework.config.conf import *

def get_sign(parmas):
	"""
	:param parmas: 读取本地pfx文件，使用私钥进行'sha256'签名
	:return: base64签名
	"""
	p12 = crypto.load_pkcs12(open(pfx_file, 'rb').read(), "123456")
	sign = crypto.sign(p12.get_privatekey(), json.dumps(parmas), "SHA256")
	b64_sign = str(base64.b64encode(sign))[2:-1]
	return b64_sign

def get_res_headers(parmas):
	"""
	:param parmas: 将请求体签名后的字节添加到请求头
	:return:签名后的请求头
	"""
	headers = {"R-Merchant": "CNZHRUIDEV"}
	headers["R-Signature"] = get_sign(parmas)
	return headers

def get_journalNumber():
	#随机生成序列号、字母+数字或者使用生成UUID作为序列号
	list = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
	journalNumber = "".join(random.sample(list, 16))

	uid = uuid.uuid4()
	jNumber = str(base64.b64encode(uid.bytes), encoding="utf-8")
	return jNumber

def get_params():
	#组装请求体参数
	params = {
		"version": "1.0",
		"journalNumber": get_journalNumber(),
		"transCode": "200001",
		"transTime": timeStamp,
		"param": {
			"payChannelCode": "CLCNWECHAT",
			"currency": "CNY",
			"amount": "-1.05",
			"productName": "POHNE",
			"productDetail": "iPhone x",
			"notifyWithReserveFiled": "Y"
		}
	}
	return params

def get_payChannelCode():
	params = {
		"version": "1.0",
		"journalNumber": get_journalNumber(),
		"transCode": "100001",
		"transTime": timeStamp,
		"param": {
			"bizType": "CL"
		}
	}
	return params

def get_orderState():
	params = {
		"version": "1.0",
		"journalNumber": get_journalNumber(),
		"transCode": "200002",
		"transTime": timeStamp,
		"param": {
			"orderJournalNumber": ""
		}
	}
	return params

def get_refund():
	"""组装从数据库获取到的参数
	:return:
	"""
	data = get_mysql_data()
	orderJournalNumber = str(data[0])
	refundAmount = str(data[1])
	params = {
		"version": "1.0",
		"journalNumber": get_journalNumber(),
		"transCode": "200003",
		"transTime": timeStamp,
		"param": {
			"orderJournalNumber": orderJournalNumber,
			"refundAmount":refundAmount,
			"refundMessage":"refund"
		}
	}
	return params

def get_mysql_data():
	"""
	从数据库查询参数，返回
	:return:
	"""
	mysql_db = My_Pymysql()
	sql = "SELECT mch_jrn_nbr,amt FROM merchant_order WHERE mch_nbr = %s and ord_status = %s"
	data = mysql_db.get_one(sql, ("CNZHRUIDEV", "A"))
	return data


def main():
	url = "http://192.168.1.1:1000/mch/trans_api"
	parmas = get_refund()
	headers = get_res_headers(parmas)
	res = requests.post(url=url, headers= headers, data=json.dumps(parmas))
	print(res.text)

if __name__ == '__main__':
	main()




