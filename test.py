import csv

if __name__ == '__main__':
    prev = "(86.1072006225586,55.2700996398926)"
    after = "POINT" + prev
    after = after.replace(',', ' ')
    print(after)
