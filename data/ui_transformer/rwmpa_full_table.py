import csv

row_template = '{S1} & {S2} & {S3} & {S4} & {S5} & {W1} & {W2} & {W3} & {W4} & {W5} & {W6} & {W7} & {W8} & {W9} & {W10} & {T1} & {T2} & {T3} & {T4} & {T5} & {T6} \\tabularnewline'

i = 1
with open('rwmpa.csv', 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        print(row_template.format(**row))