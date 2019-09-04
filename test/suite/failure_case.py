import pickle
import sys
import unittest
from interface_framework.config.conf import *


def save_failures(result,file): # file为序列化保存的文件名，配置在config/config.py中
    suite = unittest.TestSuite()
    for case_result in result.failures:  # 组装TestSuite
        print(case_result[0])
        suite.addTest(case_result[0]) # case_result是个元祖，第一个元素是用例对象，后面是失败原因等等

    with open(file,"wb") as f:
        pickle.dump(suite,f) # 序列化到指定文件



if __name__ == '__main__':
    pass
