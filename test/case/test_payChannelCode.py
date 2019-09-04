from interface_framework.libs.base_request import BaseCaseRequest
from interface_framework.libs.my_mysql import My_Pymysql
import unittest
import logging

class PayChannelCodeUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # main()
        cls.data = My_Pymysql()

    @staticmethod
    def get_test_data_calss(self):
        pass

    def setUp(self):
        pass

    def test_get_payChannelCode_CL(self):
        case_data = BaseCaseRequest("test_get_payChannelCode_CL")
        res = case_data.send_requests()
        res_data = res.json().get("result")
        logging.info(res_data)
        self.assertTrue(res_data)

    def test_get_payChannelCode_RF(self):
        case_data = BaseCaseRequest("test_get_payChannelCode_RF")
        res = case_data.send_requests()
        res_data = res.json().get("result")
        logging.info(res_data)
        self.assertTrue(res_data)

    def test_payChannelCode_is_not_exists(self):
        case_data = BaseCaseRequest("test_payChannelCode_is_not_exists")
        res = case_data.send_requests()
        res_data = res.json().get("result")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payChannelCode_is_NULL(self):
        case_data = BaseCaseRequest("test_payChannelCode_is_NULL")
        res = case_data.send_requests()
        res_data = res.json().get("result")
        logging.info(res_data)
        self.assertTrue(res_data)

    def test_payChannelCode_is_error(self):
        case_data = BaseCaseRequest("test_payChannelCode_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("result")
        expect_res = case_data.expect_res
        logging.info(res_data)
        self.assertEqual(expect_res, res_data)

if __name__ == '__main__':
    unittest.main()