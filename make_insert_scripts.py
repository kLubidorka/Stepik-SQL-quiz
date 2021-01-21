import csv


def make_table(table_name):
    with open(f'airtrans_new/{table_name}.csv', mode='r') as csv_input_file:
        with open(f'airtrans_old/{table_name}.csv', mode='w') as sql_output_file:
            csv_reader = csv.reader(csv_input_file, delimiter=',')
            writer = csv.writer(sql_output_file, delimiter=',')
            for row in csv_reader:
                writer.writerow(f'INSERT INTO {table_name} VALUES ({row});')


def make_aircrafts():
    pass


def make_all_insert_scripts():
    pass


if __name__ == '__main__':
    make_all_insert_scripts()
