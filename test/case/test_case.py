import unittest
import json
import os
import logging
from data_driver_interface_framework.config.conf import *
from data_driver_interface_framework.test.case.basecase import BaseCaseData

class PasswordWithJsonTestCase(BaseCaseData):

    def setUp(self):
        pass


    def test_test(self):
        self.send_request("baidu")

    def test_weak_password(self):
        for data in self.test_data:
            passwd = data['password']
            logging.info(passwd)
            self.assertTrue(len(passwd) >= 6)
            msg = "user %s has a weak password" %(data['name'])
            self.assertTrue(passwd != 'password', msg)
            self.assertTrue(passwd != 'password123', msg)

    def test_dummy(self):
        self.assertEqual(1,1.0)

    def test_notequal(self):
        self.assertNotEqual(1,1.0)

    def test_lessequal(self):
        self.assertLessEqual(1,3)



if __name__ == '__main__':
    unittest.main()