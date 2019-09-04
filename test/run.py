from interface_framework.utils.HTMLTestReportCN import *
from interface_framework.libs.send_email import send_email
from interface_framework.test.suite.test_suites import *
from interface_framework.test.suite.failure_case import *

def discover():
    return unittest.defaultTestLoader.discover(test_case_path)

def run(suite):
    logging.info("================================== 测试开始 ==================================")
    with open(report_file,"wb") as f:
        result = HTMLTestRunner(stream=f, title="REALPAY项目商户接口测试", description="realpay单元测试接口", tester="测试").run(suite)

    if result.failures: # 保存失败用例序列化文件
        save_failures(result, failure_case)

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

def resun_fails():
    sys.path.append(test_case_path)
    with open(failure_case,"rb") as f:
        suite = pickle.load(f)
    run(suite)

if __name__ == '__main__':
    # run_suite("smoke_sutie")
    run_all()
    # resun_fails()

