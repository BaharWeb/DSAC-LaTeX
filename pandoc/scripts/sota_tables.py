# -*- coding: utf-8 -*-
import csv
import sys
import re

TABLE_ROW_TEMPLATE = '| %s          | %s      | %s       | %s        | %s      | %s        |'
TABLE_CAPTION_TEMPLATE = 'Table: %s Evaluation {#tbl:%s-eval}'

TABLE_TEMPLATE = """| S1 Initial | S2 Web | C1 Risk | C2 Reuse | C3 Exp | C4 Agile |
| ---------- | ------ | ------- | -------- | ------ | -------- |
%s

%s"""

APPROACH_TABLE_TEMPLATE = TABLE_TEMPLATE % (TABLE_ROW_TEMPLATE, TABLE_CAPTION_TEMPLATE)

SYMBOL = {
    '0': '◯',
    '0,5': '◐',
    '1': '⬤',
}

CONSOLE_SYMBOL = {
    '0': '0',
    '0,5': '-',
    '1': '+',
}

def abbrev(string):
    abbreviations = {
        'Transformation': 'Trans',
        'Encapsulation': 'Encaps',
        'Reengineering': 'ReEng',
    }
    if string in abbreviations:
        return abbreviations[string]
    else:
        return string

data = {}
approaches = []

with open(sys.argv[1], 'r') as infile:
    reader = csv.DictReader(infile, delimiter=';')
    for row in reader:
        data[row['name'].lower()] = {
            'table': APPROACH_TABLE_TEMPLATE % (
                SYMBOL[row['init']],
                SYMBOL[row['web']],
                SYMBOL[row['risk']],
                SYMBOL[row['reuse']],
                SYMBOL[row['exp']],
                SYMBOL[row['agile']],
                row['name'],
                row['name'].replace(' ', '-'),
            ),
            'row': '| ' + row['name'] + ' | ' + row['target'] + ' | ' + abbrev(row['method']) + ' ' +
                   TABLE_ROW_TEMPLATE % (
                        SYMBOL[row['init']],
                        SYMBOL[row['web']],
                        SYMBOL[row['risk']],
                        SYMBOL[row['reuse']],
                        SYMBOL[row['exp']],
                        SYMBOL[row['agile']],
                   ) + '\n',
            'raw_data': row,
        }

table = re.compile(r"^\| S1.+?Table: (.+?) Evaluation {#tbl:.+?-eval}", re.MULTILINE | re.DOTALL)
group_start = '<!-- "SOTA-TABLE-BY-GROUP" -->'
method_start = '<!-- "SOTA-TABLE-BY-METHOD" -->'
overview_table = re.compile(group_start + '.+?{#tbl:eval-overview}', re.MULTILINE | re.DOTALL)
overview_table_methods = re.compile(method_start + '.+?{#tbl:eval-overview-methods}', re.MULTILINE | re.DOTALL)

def generate_table(match):
    approach = match.group(1).lower()
    approaches.append(approach)
    return data[approach]['table']

def substitute_table(text, sorted_approaches, regex, start, footer):
    rows = ''
    for approach in sorted_approaches:
        rows += data[approach]['row']

    text = re.sub(
        regex,
        start + '\n\n' + '| Approach | Target | Method ' + TABLE_TEMPLATE % (
            rows, footer),
        text
    )
    return text

def display_custom_table(data):
    row_format = "{:>3} {:<14} {:<6} {:<14} {:>3}" + ("{:>5} " * 6)
    print(row_format.format('ID', 'NAME', 'TARGET', 'METHOD', 'MD', 'INIT', 'WEB', 'RISK', 'REUSE', 'EXP', 'AGILE'))

    for key_value_tuple in sorted(data.items(), key=lambda kvt: kvt[1]['raw_data']['init'] +
                                                                kvt[1]['raw_data']['web'] +
                                                                kvt[1]['raw_data']['risk'] +
                                                                kvt[1]['raw_data']['reuse'] +
                                                                kvt[1]['raw_data']['exp'] +
                                                                kvt[1]['raw_data']['agile']):
        d = key_value_tuple[1]['raw_data']
        print(row_format.format(d['id'],
                                d['name'],
                                d['target'],
                                d['method'],
                                CONSOLE_SYMBOL[d['md']],
                                CONSOLE_SYMBOL[d['init']],
                                CONSOLE_SYMBOL[d['web']],
                                CONSOLE_SYMBOL[d['risk']],
                                CONSOLE_SYMBOL[d['reuse']],
                                CONSOLE_SYMBOL[d['exp']],
                                CONSOLE_SYMBOL[d['agile']]))

display_custom_table(data)

with open(sys.argv[2], 'r') as sota_text_file:
    text = sota_text_file.read()
    text = re.sub(table, generate_table, text)

    text = substitute_table(text,
                     approaches,
                     overview_table,
                     group_start,
                     'Table: Evaluation Overview {#tbl:eval-overview}')
    text = substitute_table(text,
                     sorted(approaches, key=lambda a: data[a]['raw_data']['method']),
                     overview_table_methods,
                     method_start,
                     'Table: Evaluation Overview by Method {#tbl:eval-overview-methods}')


with open(sys.argv[2], 'w') as sota_text_file:
    sota_text_file.write(text)
