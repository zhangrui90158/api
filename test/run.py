import unittest
from data_driver_interface_framework.config.conf import *
from data_driver_interface_framework.utils.HTMLTestReportCN import *
from data_driver_interface_framework.libs.send_email import send_email
from data_driver_interface_framework.test.suite.test_suites import *

def discover():
    return unittest.defaultTestLoader.discover(test_case_path)


def run(suite):
    logging.info("================================== 测试开始 ==================================")
    with open(report_file,"wb") as f:
        HTMLTestRunner(stream=f, title="Api Test", description="测试描述", tester="卡卡").run(suite)

    # send_email('report1.html')  # 发送邮件
    logging.info("================================== 测试结束 ==================================")

def run_all():
    run(discover())

def run_suite(suite_name):  # 运行`test/suite/test_suites.py`文件中自定义的TestSuite
    suite = get_sutie(suite_name)
    if suite:
        run(suite)
    else:
        print("TestSuite不存在")

if __name__ == '__main__':
    # run_suite("smoke_sutie")
    run_all()
    if send_email_table:
        send_email(report_file)
