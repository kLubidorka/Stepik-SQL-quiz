# def check(query, result):
#     if 'select' not in query.lower():
#         return False, 'Use SELECT statement to retrieve data'
#     if result['columns'] != ['model', 'range']:
#         return False, 'Incorrect names of columns'
#
#     cursor.execute("SELECT model, `range` FROM aircrafts WHERE `range` BETWEEN 1300 AND 5800 ORDER BY `range`;")
#     correct_result = cursor.fetchall()
#
#     if len(correct_result) != result['affected_rows']:
#         return False, 'Incorrect result'
#     for i in range(len(correct_result)):
#         if result['rows'][i] != list(correct_result[i]):
#             return False, 'Incorrect result'
#
#     return True

import re

if __name__ == '__main__':
    match = re.search(r'\d+', r'Decimal(\'3700.000000\')')
    print(match[0] if match else 'Not found')

    match2 = re.search(match[0], "{'_serialized.decimal': '3700.000000'}")
    print(match2[0] if match else 'Not found')
    # match = re.search(r'\d+', r'Телефон 123-12-12')
    # print(match[0] if match else 'Not found')
