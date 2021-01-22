import pymysql
from pymysql.cursors import DictCursor


def execute_statement(cursor, stmt):
    cursor.execute(stmt)


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
        execute_statement(cursor, "CREATE DATABASE IF NOT EXISTS AIRTRANS")
        execute_statement(cursor, "USE AIRTRANS")
        with open('INIT_DB.sql', mode='r') as initial_sql_script:
            sqlStatements = initial_sql_script.read().split(';')
            for statement in sqlStatements:
                if len(str.strip(statement)) != 0:
                    execute_statement(cursor, statement)
            print("database is created and filled")
        return connection
    except Exception as e:
        print("Exeception occured:{}".format(e))
        execute_statement(cursor, "DROP DATABASE AIRTRANS")
        connection.close()


if __name__ == '__main__':
    connect_to_airtrans_db()
