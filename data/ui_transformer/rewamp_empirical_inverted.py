import csv
from collections import defaultdict

row_template = '{0} & {1} & {2} & {3} & {4} & {5} & {6}\\tabularnewline'
table_data = defaultdict(list)

with open('empirical.csv', 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        for key in row:
            table_data[key].append(row[key])

for key in table_data:
    print(row_template.format(key, table_data[key][0], table_data[key][1], table_data[key][2], table_data[key][3], table_data[key][4], table_data[key][5]))