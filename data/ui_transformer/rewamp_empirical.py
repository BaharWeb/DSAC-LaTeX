import csv

row_template = '{S1} & {S2} & {S3} & {S4} & {F11} & {F12} & {F13} & {F14} & {F15} & {F21} & {F22} & {F23} & {F24} & {F25} & {Q1} & {Q2} & {Q3} & {Q4} & {Q5} & {Q6} & {W1} & {W2} & {W3} & {W4} & {W5} & {W6} & {W7} & {W8} & {W9} & {W10} & {W11}\\tabularnewline'
with open('empirical.csv', 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        print(row_template.format(**row))