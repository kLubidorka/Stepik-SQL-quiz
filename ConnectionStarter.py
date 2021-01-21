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
        sqlStatement = "USE AIRTRANS"
        cursor.execute(sqlStatement)
        with open('CREATE_TABLES.sql', mode='r') as initial_sql_script:
            sqlStatements = initial_sql_script.read().split(';')
            for statement in sqlStatements:
                if len(statement) != 0:
                    cursor.execute(statement)
            print("database is created")

        with open('INSERT_VALUES.sql', mode='r') as insert_sql_script:
            sqlStatements = insert_sql_script.read().split(';')
            for statement in sqlStatements:
                if len(statement) != 0:
                    cursor.execute(statement)
            print("database is filled")
        # sqlStatement = "INSERT INTO airports VALUES ('YKS', 'Yakutsk Airport', 'Yakutsk', ST_GeomFromText('POINT(129.77099609375 62.0932998657227)'), 'Asia/Yakutsk')"
        # cursor.execute(sqlStatement)
        # print("database is filled")
    except Exception as e:
        print("Exeception occured:{}".format(e))
    finally:
        sqlStatement = "DROP DATABASE AIRTRANS"
        cursor.execute(sqlStatement)
        connection.close()


if __name__ == '__main__':
    connect_to_airtrans_db()
