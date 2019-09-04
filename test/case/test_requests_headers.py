from interface_framework.libs.base_request import BaseCaseRequest
from interface_framework.libs.my_mysql import My_Pymysql
import unittest
import logging

class RequestsHeadersUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = My_Pymysql()

    @staticmethod
    def get_test_data_calss(self):
        pass

    def setUp(self):
        pass

    def test_requests_header_Merchant_is_not_exists(self):
        case_data = BaseCaseRequest("test_requests_header_Merchant_is_not_exists")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_requests_header_Merchant_is_null(self):
        case_data = BaseCaseRequest("test_requests_header_Merchant_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_requests_header_Signature_is_error(self):
        case_data = BaseCaseRequest("test_requests_header_Signature_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def test_requests_header_Signature_is_null(self):
        case_data = BaseCaseRequest("test_requests_header_Signature_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(res_data, expect_res)

    def assert_test(self,case_data):
        res = case_data.send_requests()
        expect_res = case_data.expect_res
        return self.assertEqual(res.json(),expect_res)



if __name__ == '__main__':
    unittest.main()


