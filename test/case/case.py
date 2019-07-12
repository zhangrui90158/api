import unittest
import json
import os
import logging
from data_driver_interface_framework.config.conf import *
from data_driver_interface_framework.test.case.base_case import BaseCaseData

class PasswordWithJsonTestCase(BaseCaseData):

    def test_test(self):
        case_data = self.get_case_data("baidu")
        self.send_request(case_data)

    def test_case(self):
        case_data = self.get_case_data("case")
        self.send_request(case_data)

    def test_get_day(self):
        case_data = self.get_case_data("get_day")
        self.send_request(case_data)

    def test_weak_password(self):
        self.assertEqual(1, 2)

    def test_dummy(self):
        self.assertEqual(1,1.0)

    def test_notequal(self):
        self.assertNotEqual(1,1.0)

    def test_lessequal(self):
        self.assertLessEqual(1,3)



if __name__ == '__main__':
    unittest.main()