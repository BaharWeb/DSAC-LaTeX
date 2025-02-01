import csv

row_template = '{i} & {c} & {d} & {t1:.0f} & {t2:.0f} & {t3:.0f} & {t4:.0f} & {t5:.0f} & {t6:.0f} & {t6c:.0f} & {t7:.0f} & {t8:.0f} & {t9:.0f} & {t10:.0f} \\tabularnewline'
#row_template = '{i} & {c} & {d} & {t1:.0f} & {t2:.0f} & {t3:.0f} & {t4:.0f} & {t5:.0f} \\tabularnewline'
#row_template = '{i} & {t6:.0f} & {t7:.0f} & {t8:.0f} & {t9:.0f} & {t10:.0f} \\tabularnewline'

i = 1
with open('benchmarks_compiled_noht.csv', 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        row['i'] = i
        i += 1
        times = ['t' + str(i + 1)for i in range(10)]
        for t in times:
            row[t] = float(row[t])
        row['t6c'] = float(row['t6c'])

        print(row_template.format(**row))