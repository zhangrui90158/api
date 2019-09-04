from interface_framework.libs.base_request import BaseCaseRequest
from interface_framework.libs.my_mysql import My_Pymysql
import unittest
import logging

class OrderStateUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # main()
        cls.data = My_Pymysql()

    @staticmethod
    def get_test_data_calss(self):
        pass

    def setUp(self):
        pass

    def test_CLCNWECHAT_ORDERSTATE_fail(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDERSTATE_fail")
        res = case_data.send_requests()
        res_data = res.json().get("result").get("orderStatus")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_ORDERSTATE_succeed(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDERSTATE_succeed")
        res = case_data.send_requests()
        res_data = res.json().get("result").get("orderStatus")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_ORDERSTATE_accept(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDERSTATE_accept")
        res = case_data.send_requests()
        res_data = res.json().get("result")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_ORDERSTATE_processed(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDERSTATE_processed")
        res = case_data.send_requests()
        res_data = res.json().get("result")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_ORDER_is_null(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDER_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_ORDER_is_unauthorized(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_ORDER_is_unauthorized")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)


if __name__ == '__main__':
    unittest.main()