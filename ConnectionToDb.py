import pymysql
from pymysql.cursors import DictCursor

tablename = "AIRTRANS"


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
        with connection.cursor() as cursor:
            execute_statement(cursor, f"CREATE DATABASE IF NOT EXISTS {tablename}")
            execute_statement(cursor, f"USE {tablename}")
            with open('INIT_DB.sql', mode='r') as initial_sql_script:
                sqlStatements = initial_sql_script.read().split(';')
                for statement in sqlStatements:
                    if len(str.strip(statement)) != 0:
                        execute_statement(cursor, statement)
                print("database is created and filled")
    except Exception as e:
        print("Exeception occured:{}".format(e))
    return connection


def release_resources(connection):
    with connection.cursor() as cursor:
        execute_statement(cursor, f"DROP DATABASE {tablename}")
    connection.close()


def main():
    connection = connect_to_airtrans_db()
    release_resources(connection)


if __name__ == '__main__':
    main()
