from interface_framework.libs.base_request import BaseCaseRequest
from interface_framework.libs.my_mysql import My_Pymysql
import unittest
import logging

class AccountBillUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # main()
        cls.data = My_Pymysql()

    @staticmethod
    def get_test_data_calss(self):
        pass

    def setUp(self):
        pass

    def test_cl_account_bill_exists(self):
        case_data = BaseCaseRequest("test_cl_account_bill_exists")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        self.assertTrue(res_data)

    def test_cl_account_bill_not_exists(self):
        case_data = BaseCaseRequest("test_cl_account_bill_not_exists")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_account_bill_settleDateformat_is_error(self):
        case_data = BaseCaseRequest("test_account_bill_settleDateformat_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_account_bill_settleDate_is_null(self):
        case_data = BaseCaseRequest("test_account_bill_settleDate_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_rf_account_bill_exists(self):
        case_data = BaseCaseRequest("test_rf_account_bill_exists")
        res = case_data.send_requests()
        res_data = res.json().get("result")
        logging.info(res_data)
        self.assertTrue(res_data)

    def test_rf_account_bill_not_exists(self):
        case_data = BaseCaseRequest("test_rf_account_bill_not_exists")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_account_bill_bizType_is_null(self):
        case_data = BaseCaseRequest("test_account_bill_bizType_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_account_bill_bizType_is_error(self):
        case_data = BaseCaseRequest("test_account_bill_bizType_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)


if __name__ == '__main__':
    unittest.main()


