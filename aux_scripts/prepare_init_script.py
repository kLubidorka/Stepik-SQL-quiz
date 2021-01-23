import csv
import os


def insert_into_table(table_name):
    with open(f'airtrans_new/{table_name}.csv', mode='r') as csv_input_file, \
            open('sql/INSERT_VALUES.sql', mode='a') as sql_output_file:
        csv_reader = csv.reader(csv_input_file, delimiter=',')
        for row in csv_reader:
            if table_name == 'airports':
                sql_output_file.write(
                    f"INSERT INTO {table_name} VALUES ('{row[0]}', '{row[1]}', '{row[2]}', ST_GeomFromText({row[3]}), '{row[4]}');\n")
            elif table_name == 'flights':
                row8 = f"'{row[8]}'" if row[8] != '' else "NULL"
                row9 = f"'{row[9]}'" if row[9] != '' else "NULL"
                sql_output_file.write(
                    f"INSERT INTO {table_name} VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', {row8}, {row9});\n")
            else:
                sql_output_file.write(f'INSERT INTO {table_name} VALUES ({str(row)[1:-1]});\n')


def add_all_insert_scripts():
    try:
        os.remove('sql/INSERT_VALUES.sql')
    except OSError as e:
        print(e)
    insert_into_table('bookings')
    insert_into_table('airports')
    insert_into_table('aircrafts')
    insert_into_table('seats')
    insert_into_table('tickets')
    insert_into_table('flights')
    insert_into_table('ticket_flights')
    insert_into_table('boarding_passes')


if __name__ == '__main__':
    add_all_insert_scripts()
