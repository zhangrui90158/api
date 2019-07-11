import pymysql
from data_driver_interface_framework.config.conf import *

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
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self,sql):
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

