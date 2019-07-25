import pymysql
from interface_framework.config.conf import *

class MyMysql():
    def __init__(self):
        self.conn = pymysql.connect(
            host = db_host,
            port = db_port,
            user = db_user,
            passwd = db_passwd,
            db = db,
            charset = "utf8"
        )
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self,sql):
        '''
        :param sql: 传入sql参数
        :return: 返回查询的所有结果
        '''
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self,sql):
        '''
        :param sql: 传入sql参数，提交sql执行
        :return:
        '''
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

if __name__ == '__main__':
    data = MyMysql()
    sql = "select * from bookinfo"
    result = data.query(sql)


