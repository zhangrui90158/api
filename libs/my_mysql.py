import pymysql
from interface_framework.config.conf import mysql_options

class My_Pymysql():
    def __init__(self):
        self.conn = pymysql.connect(**mysql_options)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def __edit(self,sql,*args):
        count = 0
        try:
            count = self.cur.execute(sql,*args)
            self.conn.commit()
        except Exception as e:
            print(e)
        return count

    def get_one(self,sql,*args):
        result = None
        try:
            self.cur.execute(sql,*args)
            result = self.cur.fetchone()
        except Exception as e:
            print(e)
        return result

    def get_all(self, sql,*args):
        result = []
        try:
            self.cur.execute(sql,*args)
            result = self.cur.fetchall()
        except Exception as e:
            print(e)
        return result

    def insert(self, sql, *args):
        return self.__edit(sql, *args)

    def update(self, sql, *args):
        return self.__edit(sql, *args)

    def delete(self, sql, *args):
        return self.__edit(sql, *args)


if __name__ == '__main__':
    data = My_Pymysql()
    sql = "SELECT mch_jrn_nbr,amt FROM merchant_order WHERE mch_nbr = %s and ord_status = %s"
    # sql = 'insert into houses (title,position,price,score,comments) values (%s,%s,%s,%s,%s)'
    result = data.get_one(sql,("CNZHRUIDEV","S"))

    print(result[1])