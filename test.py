import csv

if __name__ == '__main__':
    with open('airtrans_new/bookings.csv', mode='r') as csv_file:
        valid_book_refs = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            valid_book_refs.append(row[0])
        print(valid_book_refs)
