import csv
import json


# К каждой строке из таблицы 'table_name' применяется функция 'row_updater'
# Затем обновленная таблица сохраняется в папку 'airtrans_new'
def update_table(table_name, row_updater):
    with open(f'airtrans_new/{table_name}.csv', mode='w') as csv_output_file:
        with open(f'airtrans_old/{table_name}.csv', mode='r') as csv_input_file:
            csv_reader = csv.reader(csv_input_file, delimiter=',')
            writer = csv.writer(csv_output_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                new_row = row_updater(row)
                if new_row != "":
                    writer.writerow(new_row)
                line_count += 1
            print(f'Processed {line_count} lines.')


# Вместо JSON оставляем один его элемент для упрощения
def update_aircrafts():
    def update_row_aircrafts(row):
        row[1] = json.loads(row[1])["en"]
        return row

    update_table('aircrafts', update_row_aircrafts)


# Вместо JSON оставляем один его элемент для упрощения
def update_airports():
    def update_row_airports(row):
        row[1] = json.loads(row[1])["en"]
        row[2] = json.loads(row[2])["en"]
        return row

    update_table('airports', update_row_airports)


# Вместо JSON оставляем один его элемент для упрощения
def update_tickets():
    def update_row_tickets(row):
        row[4] = json.loads(row[4])["phone"]
        return row

    update_table('tickets', update_row_tickets)


# Сокращаем размер таблицы
def update_bookings():
    def update_row_bookings(row):
        if row[0] > "001269":
            return ""
        return row

    update_table('bookings', update_row_bookings)


def update_all_csv_files():
    # update_aircrafts()
    # update_airports()
    # update_tickets()
    update_bookings()


if __name__ == '__main__':
    update_all_csv_files()
