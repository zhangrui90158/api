import pymysql
from interface_framework.config.conf import *

#获取连接方法
def get_db_mysql():
    conn = pymysql.connect(host=db_host,
                    port=db_port,
                    user=db_user,
                    passwd=db_passwd,   # password也可以
                    db=db,
                    charset='utf8')
    return conn

# 封装数据库查询操作
def query_sql(sql):
    conn = get_db_mysql()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return  result


# 封装更改数据库操作
def update_sql(sql):
    conn = get_db_mysql()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    sql = "select * from bookinfo"
    result = query_sql(sql)
    print(result)


