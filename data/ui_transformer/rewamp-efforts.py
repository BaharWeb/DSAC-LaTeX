import csv

row_template = '{ec31} & {eu31} & {ed31} & {ec32} & {eu32} & {ed32} & {ec41} & {eu41} & {ed41} & {ec42} & {eu42} & {ed42} & {ec51} & {eu51} & {ed51} & {ec52} & {eu52} & {ed52} & {ec61} & {eu61} & {ed61} & {ec62} & {eu62} & {ed62}  \\tabularnewline'
with open('rewamp-efforts.csv', 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        print(row_template.format(**row))