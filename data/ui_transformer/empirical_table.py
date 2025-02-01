import csv

row_template = '{Layout} & {Combination} & {Q1} & {Q2} & {Q3} & {Q4} & {Q5} & {Q6} & {Q7} & {Mean}\\tabularnewline'

with open('average_over_persons.csv', 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        row['Layout'] = row['ID'].split('_')[0]
        row['Combination'] = row['ID'].split('_')[1]
        questions = ['Q' + str(i + 1)for i in range(7)]
        values = [float(row[index]) for index in questions]
        row['Mean'] = round(sum(values)/len(values), 2)
        print(row_template.format(**row))