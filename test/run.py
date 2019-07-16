from interface_framework.config.conf import *
from interface_framework.utils.HTMLTestReportCN import *
from interface_framework.libs.send_email import send_email
from interface_framework.test.suite.test_suites import *

def discover():
    return unittest.defaultTestLoader.discover(test_case_path)


def run(suite):
    logging.info("================================== 测试开始 ==================================")
    with open(report_file,"wb") as f:
        HTMLTestRunner(stream=f, title="项目接口测试 Test", description="测试描述", tester="测试名字").run(suite)

    # send_email('report1.html')  # 发送邮件
    if send_email_label:
        send_email(report_file)
    logging.info("================================== 测试结束 ==================================")

def run_all():
    run(discover())

def run_suite(suite_name):  # 运行`debug/suite/test_suites.py`文件中自定义的TestSuite
    suite = get_sutie(suite_name)
    if suite:
        run(suite)
    else:
        print("TestSuite不存在")

if __name__ == '__main__':
    # run_suite("smoke_sutie")
    run_all()

