import csv
import json

valid_book_refs = ['00000F', '000012', '000068', '000181', '0002D8', '0002DB', '0002E0', '0002F3', '00034E', '000352',
                   '000374', '00044D', '00044E', '0004B0', '0004E1', '000511', '00053F', '00054E', '0005E7', '0005F4',
                   '0005FF', '00067B', '0006C3', '0006F5', '000735', '000769', '000784', '0007A9', '0007ED', '0007FC',
                   '000836', '000842', '000859', '000862', '0008DF', '0008F4', '0008FD', '000909', '000917', '00094B',
                   '00098F', '000999', '0009D5', '0009ED', '000A1E', '000A39', '000AA7', '000AB3', '000ADA', '000B77',
                   '000B91', '000B97', '000BB3', '000BD8', '000BFF', '000C28', '000C2B', '000D3C', '000DBE', '000DC5',
                   '000E07', '000E3A', '000EA2', '000EFA', '000F07', '000F74', '000F7D', '000FAC', '000FD6', '00101D',
                   '00107C', '001089', '00111B', '00114E', '001164', '001184', '001191', '0011A9', '001233', '001269']

valid_ticket_nos = ['0005432034627', '0005432034628', '0005432034629', '0005432081476', '0005432081477',
                    '0005432106361', '0005432106386', '0005432133238', '0005432133239', '0005432133240',
                    '0005432262420', '0005432293273', '0005432328074', '0005432329491', '0005432329492',
                    '0005432359741', '0005432383559', '0005432460830', '0005432460831', '0005432527326',
                    '0005432528533', '0005432528534', '0005432529127', '0005432529998', '0005432531066',
                    '0005432531067', '0005432604244', '0005432660797', '0005432663023', '0005432706449',
                    '0005432706450', '0005432747729', '0005432891015', '0005432891016', '0005433009535',
                    '0005433036153', '0005433036154', '0005433036155', '0005433101280', '0005433151107',
                    '0005433192917', '0005433192918', '0005433192919', '0005433202287', '0005433342102',
                    '0005433342103', '0005433368030', '0005433368031', '0005433435011', '0005433634101',
                    '0005433722400', '0005433763203', '0005433785757', '0005433806172', '0005433846486',
                    '0005433867776', '0005433869064', '0005433869065', '0005433925347', '0005433986059',
                    '0005433986060', '0005433986395', '0005433986733', '0005433986734', '0005434022883',
                    '0005434022884', '0005434023206', '0005434023207', '0005434067063', '0005434067064',
                    '0005434069385', '0005434139997', '0005434139998', '0005434407173', '0005434407174',
                    '0005434444152', '0005434444153', '0005434448293', '0005434448294', '0005434480541',
                    '0005434480542', '0005434550605', '0005434550606', '0005434655397', '0005434993985',
                    '0005435070028', '0005435070029', '0005435127439', '0005435127440', '0005435177476',
                    '0005435214478', '0005435254536', '0005435286696', '0005435372110', '0005435375058',
                    '0005435377920', '0005435423700', '0005435424469', '0005435424470', '0005435425341',
                    '0005435541622', '0005435545944', '0005435545945', '0005435614475', '0005435653688',
                    '0005435653907', '0005435706114', '0005435706115', '0005435767739', '0005435767874',
                    '0005435788796', '0005435790266', '0005435790267', '0005435808109', '0005435838975']

valid_flight_ids = []


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


# Сокращаем размер таблицы
def update_tickets_2():
    def update_row_tickets(row):
        if row[1] in valid_book_refs:
            valid_ticket_nos.append(row[0])
            return row
        return ""

    update_table('tickets', update_row_tickets)


# Сокращаем размер таблицы
def update_boarding_passes():
    def update_row_boarding_passes(row):
        if row[0] in valid_ticket_nos:
            return row
        return ""

    update_table('boarding_passes', update_row_boarding_passes)


# Сокращаем размер таблицы
def update_ticket_flights():
    def update_row_ticket_flights(row):
        if row[0] in valid_ticket_nos:
            valid_flight_ids.append(row[1])
            return row
        return ""

    update_table('ticket_flights', update_row_ticket_flights)


def update_all_csv_files():
    # update_aircrafts()
    # update_airports()
    # update_tickets()
    # update_bookings()
    # update_tickets_2()
    # update_boarding_passes()
    update_ticket_flights()


if __name__ == '__main__':
    update_all_csv_files()
