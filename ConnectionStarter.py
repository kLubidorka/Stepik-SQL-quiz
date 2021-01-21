import pymysql
from pymysql.cursors import DictCursor


def connect_to_airtrans_db():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='password',
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        cursor = connection.cursor()
        sqlStatement = "CREATE DATABASE IF NOT EXISTS AIRTRANS"
        cursor.execute(sqlStatement)
    except Exception as e:
        print("Exeception occured:{}".format(e))
    finally:
        connection.close()


if __name__ == '__main__':
    connect_to_airtrans_db()
