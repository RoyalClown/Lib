import cx_Oracle

oracle_url = "uuplatformdemo/selectuuplatform@192.168.253.6/orcl"


class OracleConnection:
    # 存储数据
    def __init__(self, ):
        self.conn = cx_Oracle.connect(oracle_url)

    # 接受处理之后的数据data
    def update(self, sql):
        cursor = self.conn.cursor()
        alter_data = cursor.execute(sql)
        cursor.close()
        return alter_data

    # 接受处理之后的数据data
    def insert(self, sql):
        cursor = self.conn.cursor()
        insert_data = cursor.execute(sql)
        cursor.close()
        return insert_data

    def close_connection(self):
        self.conn.close()
