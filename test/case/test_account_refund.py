from interface_framework.libs.base_request import BaseCaseRequest
from interface_framework.libs.my_mysql import My_Pymysql
import unittest
import logging

class AccountRefundUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # main()
        cls.data = My_Pymysql()

    @staticmethod
    def get_test_data_calss(self):
        pass

    def setUp(self):
        pass

    def test_CLCNWECHAT_refund_order_is_unauthorized(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_refund_order_is_unauthorized")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_refund_order_is_not_exists(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_refund_order_is_not_exists")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_refund_order_is_not_null(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_refund_order_is_not_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_refund_order_state_is_P(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_refund_order_state_is_P")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_refund_order_state_is_F(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_refund_order_state_is_F")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_refundAmount_is_error(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_refundAmount_is_error")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_refundAmount_order_is_exists(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_refundAmount_order_is_exists")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_refundAmount_is_null(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_refundAmount_is_null")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def test_CLCNWECHAT_refundAmount_is_minus(self):
        case_data = BaseCaseRequest("test_CLCNWECHAT_refundAmount_is_minus")
        res = case_data.send_requests()
        res_data = res.json().get("code")
        logging.info(res_data)
        expect_res = case_data.expect_res
        self.assertEqual(expect_res, res_data)

    def assert_test(self,case_data):
        res = case_data.send_requests()
        expect_res = case_data.expect_res
        return self.assertEqual(res.json(),expect_res)



if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(MyUnittest("test_payChannelCode_is_CLCNWECHAT"))
    # unittest.TextTestRunner(verbosity=3).run(suite)
    suite = unittest.makeSuite(MyUnittest,"test_payChannelCode_is_CLCNWECHAT")
    unittest.TextTestRunner(verbosity=2).run(suite)

