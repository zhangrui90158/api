import requests
import json
import random
import base64
import uuid
from OpenSSL import crypto
from interface_framework.libs.my_mysql import My_Pymysql
from interface_framework.config.conf import *
from multiprocessing import Manager,Process,Pool

def get_sign(params):
	"""
	:parmas: 读取本地pfx文件，使用私钥进行'sha256'签名
	:return: base64签名
	"""
	with open(pfx_file, 'rb') as f:
		p12 = crypto.load_pkcs12(f.read(), "123456")
		sign = crypto.sign(p12.get_privatekey(), json.dumps(params).encode("utf-8"), "SHA256")
		b64_sign = str(base64.b64encode(sign))[2:-1]
		return b64_sign

def get_verify(res_params):
	with open(pfx_file, 'rb') as f:
		p12 = crypto.load_pkcs12(f.read(), "123456")
		signature = crypto.sign(p12.get_privatekey(),json.dumps(res_params),"SHA256")
		result = crypto.verify(p12.get_certificate(),signature,json.dumps(res_params),"SHA256")
		return result

def get_res_headers(params):
	"""
	:param parmas: 将请求体签名后的字节添加到请求头
	:return:签名后的请求头
	"""
	headers = {"R-Merchant": "CNZHRUIDEV"}
	headers["R-Signature"] = get_sign(params)
	return headers

def get_journalNumber():
	#随机生成序列号、字母+数字或者使用生成UUID作为序列号
	list = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
	journalNumber = "".join(random.sample(list, 16))

	uid = uuid.uuid4()
	jNumber = str(base64.b64encode(uid.bytes), encoding="utf-8")
	return jNumber

def get_pay_params():
	#组装请求体参数
	params = {
		"version": "1.0",
		"journalNumber":get_journalNumber(),
		"transCode": "200001",
		"transTime": timeStamp,
		"endpointIp":"192.168.1.153",
		"notifyUrl":"http://localhost:5000/api/pay",
		"param": {
			"payChannelCode": "CLCNWECHAT",
			"currency": "CNY",
			"amount": "0.20",
			"productName": "POHNE",
			"productDetail": "iPhone x",
			"notifyWithReserveFiled": "Y"
		}
	}
	return params

def get_payChannelCode():
	params = {
		"version": "",
		"journalNumber": "",
		"transCode": "100001",
		"transTime": timeStamp,
		"endpointIp": "192.168.1.153",
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
		"endpointIp": "192.168.1.153",
		"param": {
			"orderJournalNumber": "201908061001"
		}
	}
	return params

def get_refund_params():
	"""组装从数据库获取到的参数
	:return:
	"""
	# data = get_mysql_data()
	# orderJournalNumber = str(data[0])
	# refundAmount = str(data[1])
	params = {
		"version": "1.0",
		"journalNumber": get_journalNumber(),
		"transCode": "200003",
		"transTime": timeStamp,
		"notifyUrl": "http://localhost:5000/api/refund",
		"endpointIp": "192.168.1.153",
		"param": {
			"orderJournalNumber": "iZYB9gE6QG+YjcFEtJNCpg==",
			"refundAmount":"0.20",
			"refundMessage":"refund"
		}
	}
	return params

def get_clearing_file():
	params = {
		"version": "1.0",
		"journalNumber": get_journalNumber(),
		"transCode": "200004",
		"transTime": timeStamp,
		"endpointIp": "192.168.1.153",
		"param": {
			"settleDate": "20190807",
			"bizType":"CL"
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
	data = mysql_db.get_one(sql, ("CNZHRUIDEV", "S"))
	return data

def send_requests(queue):
	url = "http://123.207.250.215:9000/mch/trans_api"
	# params = get_payChannelCode()
	# params = get_pay_params()
	# params = get_orderState()
	# params = get_refund_params()
	params = get_clearing_file()
	headers = get_res_headers(params)
	res = requests.post(url= url, headers= headers, data= json.dumps(params))
	print(res.json())
	queue.put(res)
	# verify = get_verify(res.text)
	# print(verify)

def main():
	pool = Pool(4)
	queue = Manager().Queue()
	for i in range(1):
		pool.apply_async(send_requests,args=(queue,))
	pool.close()
	pool.join()


if __name__ == '__main__':
	main()





