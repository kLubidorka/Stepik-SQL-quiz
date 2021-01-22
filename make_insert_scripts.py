import csv
import os


def make_table(table_name):
    with open(f'airtrans_new/{table_name}.csv', mode='r') as csv_input_file, \
            open('sql/INSERT_VALUES.sql', mode='a') as sql_output_file:
        csv_reader = csv.reader(csv_input_file, delimiter=',')
        for row in csv_reader:
            if table_name == 'airports':
                sql_output_file.write(
                    f"INSERT INTO {table_name} VALUES ('{row[0]}', '{row[1]}', '{row[2]}', {row[3]}, '{row[4]}');\n")
            elif table_name == 'flights':
                temp8 = f"'{row[8]}'" if row[8] != '' else "NULL"
                temp9 = f"'{row[9]}'" if row[9] != '' else "NULL"
                sql_output_file.write(
                    f"INSERT INTO {table_name} VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', {temp8}, {temp9});\n")
            else:
                sql_output_file.write(f'INSERT INTO {table_name} VALUES ({str(row)[1:-1]});\n')


def make_all_insert_scripts():
    try:
        os.remove('sql/INSERT_VALUES.sql')
    except OSError:
        pass
    make_table('bookings')
    make_table('airports')
    make_table('aircrafts')
    make_table('seats')
    make_table('tickets')
    make_table('flights')
    make_table('ticket_flights')
    make_table('boarding_passes')


if __name__ == '__main__':
    make_all_insert_scripts()
