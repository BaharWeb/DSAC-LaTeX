import csv

row_template = '{T1} & {T2} & {T31} & {T41} & {T51} & {T61} & {T71} & {T32} & {T42} & {T52} & {T62} & {T72} \\tabularnewline'
with open('rewamp-times.csv', 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        print(row_template.format(**row))