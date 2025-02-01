import csv

row_template = '{A01} & {A02} & {A03} & {A11} & {A12} & {A13} & {A21} & {A22} & {A23} & {A31} & {A32} & {A33} & {Afav} & {B01} & {B02} & {B03} & {B11} & {B12} & {B13} & {B21} & {B22} & {B23} & {B31} & {B32} & {B33} & {Bfav} & {C01} & {C02} & {C03} & {C11} & {C12} & {C13} & {C21} & {C22} & {C23} & {C31} & {C32} & {C33} & {Cfav} \\tabularnewline'
with open('ci.full.csv', 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        print(row_template.format(**row))