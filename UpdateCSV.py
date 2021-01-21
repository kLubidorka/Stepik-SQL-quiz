import csv
import json


def update_table(table_name, row_updater, row_limit):
    with open(f'airtrans_new/{table_name}.csv', mode='w') as csv_output_file:
        with open(f'airtrans_old/{table_name}.csv', mode='r') as csv_input_file:
            csv_reader = csv.reader(csv_input_file, delimiter=',')
            writer = csv.writer(csv_output_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                writer.writerow(row_updater(row))
                line_count += 1
                if line_count >= row_limit:
                    break
            print(f'Processed {line_count} lines.')


def update_all_csv_files():
    def update_row_aircrafts(row):
        row[1] = json.loads(row[1])["en"]
        return row

    update_table('aircrafts', update_row_aircrafts, 100)


if __name__ == '__main__':
    update_all_csv_files()
