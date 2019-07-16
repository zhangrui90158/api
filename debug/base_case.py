import unittest
import json
from conf import *
import requests
import logging

class BaseCaseData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_file = os.path.join(data_path, "data.json")
        with open(cls.data_file, "r") as f:
            cls.test_data = json.load(f)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def get_case_name(self,case_name):
        return self.test_data.get(case_name)

    def get_case_data(self,case_name):
        return self.test_data.get(case_name)

    def send_request(self,case_data):
        # case_name = self.get_case_data(case_name)
        headers = case_data.get('headers')
        url = case_data.get('url')
        method = case_data.get('method')
        args = case_data.get('args')
        expect_res = case_data.get('expect_res')
        data_type = case_data.get('data_type')
        logging.info('url = {0}+ \n + args = {1} + \n + method = {2}'.format(url,args,method))

        if method.upper() == "GET":
            if not args:
                res = requests.get(url= url)
                logging.info(res.status_code)
                self.assertEqual(expect_res,res.status_code)
            else:
                res = requests.get(url= url, params= args)
                logging.info(res.status_code)
                self.assertEqual(expect_res, res.status_code)

        elif method.upper() == "POST" and data_type.upper() == "APPLICATION/JSON":
            res = requests.post(url=url, json=json.loads(args), headers=json.loads(headers))  # JSON格式请求
            logging.info( url, args, json.dumps(json.loads(expect_res), sort_keys=True),
                         json.dumps(res.json(), ensure_ascii=False, sort_keys=True))
            self.assertDictEqual(res.json(), json.loads(expect_res))

        elif method.upper() == "POST" and data_type.upper() == "FROM":
            res = requests.post(url= url, data= json.loads(args), headers = json.loads(headers))
            logging.info(url,args,expect_res,res.text)
            self.assertEqual(expect_res,res.text)

if __name__ == '__main__':
    unittest.main()