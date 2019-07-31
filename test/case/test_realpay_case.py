from interface_framework.test.case.basecase import BaseCaseRequest
from interface_framework.libs.my_mysql import My_Pymysql
import unittest
import logging


class MyUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # main()
        cls.data = My_Pymysql()

    @staticmethod
    def get_test_data_calss(self):
        pass

    def setUp(self):
        pass

    def test_payChannelCode_is_CLCNWECHAT(self):
        case_data = BaseCaseRequest("test_payChannelCode_is_CLCNWECHAT")
        res = case_data.send_requests()
        res_data = res.json().get("result")[0]
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_payChannelCode_is_CLVNMOMOPAY(self):
        case_data = BaseCaseRequest("test_payChannelCode_is_CLVNMOMOPAY")
        res = case_data.send_requests()
        res_data = res.json().get("result")[1]
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_payChannelCode_is_RFCNWECHAT(self):
        case_data = BaseCaseRequest("test_payChannelCode_is_RFCNWECHAT")
        res = case_data.send_requests()
        res_data = res.json().get("result")[0]
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_payChannelCode_is_RFVNMOMOPAY(self):
        case_data = BaseCaseRequest("test_payChannelCode_is_RFVNMOMOPAY")
        res = case_data.send_requests()
        res_data = res.json().get("result")[1]
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_payChannelCode_is_NULL(self):
        case_data = BaseCaseRequest("test_payChannelCode_is_NULL")
        res = case_data.send_requests()
        res_data = res.json().get("result")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_CLCNWECHAT(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_CLCNWECHAT_payChannelCode_is_null(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_payChannelCode_is_null")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_CLCNWECHAT_CNY_notis_amount(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_CNY_notis_amount")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_CLCNWECHAT_amount_is_minus(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_amount_is_minus")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_CLCNWECHAT_ORDERSTATE_fail(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDERSTATE_fail")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_CLCNWECHAT_ORDERSTATE_succeed(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDERSTATE_succeed")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_CLCNWECHAT_ORDERSTATE_accept(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDERSTATE_accept")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_CLCNWECHAT_ORDERSTATE_processed(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDERSTATE_processed")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_CLCNWECHAT_ORDER_is_null(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDER_is_null")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_CLCNWECHAT_ORDER_is_unauthorized(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDER_is_unauthorized")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_CLCNWECHAT_refund(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_refund")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)



    def assert_test(self,case_data):
        res = case_data.send_requests()
        expect_res = case_data.expect_res
        return self.assertEqual(res.json(),expect_res)

if __name__ == '__main__':
    unittest.main()

