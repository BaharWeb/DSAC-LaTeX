import csv

row_template = '{t21} & {t41} & {t61} & {t101} & {t111} & {t131} & {t151} & {t161} & {t22} & {t42} & {t62} & {t102} & {t112} & {t132} & {t152} & {t162} \\tabularnewline'
with open('rwmpa-times.csv', 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        print(row_template.format(**row))