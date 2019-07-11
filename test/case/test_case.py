import unittest
import json
import os
import logging
from data_driver_interface_framework.config.conf import *
from data_driver_interface_framework.test.case.base_case import BaseCaseData

class PasswordWithJsonTestCase(BaseCaseData):

    def test_test(self):
        self.send_request("baidu")

    def test_case(self):
        self.send_request("case")

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