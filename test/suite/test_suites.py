from data_driver_interface_framework.test.case.case import PasswordWithJsonTestCase
import unittest

smoke_sutie = unittest.TestSuite()
# smoke_sutie.addTest([PasswordWithJsonTestCase('test_test'),PasswordWithJsonTestCase('test_weak_password')])

def get_sutie(sutie_name):
    return globals().get(sutie_name)