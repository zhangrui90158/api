from interface_framework.libs.base_request import BaseCaseRequest
from interface_framework.libs.my_mysql import My_Pymysql
import unittest
import logging

class PaymentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # main()
        cls.data = My_Pymysql()

    @staticmethod
    def get_test_data_calss(self):
        pass

    def setUp(self):
        pass

    def test_account_bill_bizType_is_error(self):
        case_data = BaseCaseRequest("test_account_bill_bizType_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payment_currency_is_error(self):
        case_data = BaseCaseRequest("test_payment_currency_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payment_currency_is_over_length(self):
        case_data = BaseCaseRequest("test_payment_currency_is_over_length")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payment_amount_is_null(self):
        case_data = BaseCaseRequest("test_payment_amount_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payment_amount_is_error(self):
        case_data = BaseCaseRequest("test_payment_amount_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payment_amount_is_empty(self):
        case_data = BaseCaseRequest("test_payment_amount_is_empty")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payeeAccount_is_null(self):
        case_data = BaseCaseRequest("test_payeeAccount_is_null")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payeeAccount_is_empty(self):
        case_data = BaseCaseRequest("test_payeeAccount_is_empty")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    @unittest.skip("tiaoguo")
    def test_payeeAccount_is_error(self):
        case_data = BaseCaseRequest("test_payeeAccount_is_error")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payeeType_is_not_exits(self):
        case_data = BaseCaseRequest("test_payeeType_is_not_exits")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payeeType_is_not_null(self):
        case_data = BaseCaseRequest("test_payeeType_is_not_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payeeType_is_not_empty(self):
        case_data = BaseCaseRequest("test_payeeType_is_not_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payeeType_is_not_over_length(self):
        case_data = BaseCaseRequest("test_payeeType_is_not_over_length")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payeeName_is_null(self):
        case_data = BaseCaseRequest("test_payeeName_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    @unittest.skip("跳过")
    def test_payeeName_is_error(self):
        case_data = BaseCaseRequest("test_payeeName_is_error")
        res = case_data.send_requests()
        res_data = res.json()
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_payeeName_is_empty(self):
        case_data = BaseCaseRequest("test_payeeName_is_empty")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)
if __name__ == '__main__':
    unittest.main()


