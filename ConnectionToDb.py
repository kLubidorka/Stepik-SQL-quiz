import pymysql
from pymysql.cursors import DictCursor

tablename = "AIRTRANS"


def execute_statement(connection, stmt, commit=False):
    connection.cursor().execute(stmt)
    if commit:
        connection.commit()


def connect_to_airtrans_db():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='password',
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        execute_statement(connection, f"CREATE DATABASE IF NOT EXISTS {tablename}")
        execute_statement(connection, f"USE {tablename}")
        with open('INIT_DB.sql', mode='r') as initial_sql_script:
            sqlStatements = initial_sql_script.read().split(';')
            for statement in sqlStatements:
                if len(str.strip(statement)) != 0:
                    execute_statement(connection, statement)
            connection.commit()
            print("database is created and filled")

    except Exception as e:
        print("Exeception occured:{}".format(e))
    return connection


def release_resources(connection):
    execute_statement(connection, f"DROP DATABASE {tablename}", commit=True)
    connection.close()


def main():
    connection = connect_to_airtrans_db()
    release_resources(connection)


if __name__ == '__main__':
    main()
