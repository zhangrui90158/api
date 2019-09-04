from interface_framework.libs.base_request import BaseCaseRequest
from interface_framework.libs.my_mysql import My_Pymysql
import unittest
import logging

class WechatOrderUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # main()
        cls.data = My_Pymysql()

    @staticmethod
    def get_test_data_calss(self):
        pass

    def setUp(self):
        pass

    def test_CLCNWECHAT_create_order(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_create_order")
        res = case_data.send_requests()
        res_data = res.json().get("result")
        logging.info(res_data)
        self.assertTrue(res_data)

    @unittest.skip("暂时不执行")
    def test_CLVNMOMOPAY_order(self):
        case_data = BaseCaseRequest("test_CLVNMOMOPAY_order")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_payChannelCode_is_null(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_payChannelCode_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_payChannelCode_is_error(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_payChannelCode_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_amount_is_null(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_amount_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info("test_CLCNWECHAT_CNY_not_is_amount res_data={}".format(res_data))
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_amount_is_int(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_amount_is_int")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        self.assertTrue(res_data)

    def test_CLCNWECHAT_amount_is_minus(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_amount_is_minus")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_amount_is_error(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_amount_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_amount_is_overlength(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_amount_is_overlength")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_currency_is_error(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_currency_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_currency_is_null(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_currency_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_expireTime_is_null(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_expireTime_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_expireTime_is_error(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_expireTime_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_expireTime_is_less(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_expireTime_is_less")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

if __name__ == '__main__':
    unittest.main()