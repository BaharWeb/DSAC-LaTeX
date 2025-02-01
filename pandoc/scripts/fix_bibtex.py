import sys
import calendar
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *
from titlecase import titlecase


REMOVE_KEYS = ['annote', 'file', 'mendeley-tags', 'abstract']

month_table = {v.lower(): k for k,v in enumerate(calendar.month_abbr)}

REMOVE_DASH_FROM_ISBN = str.maketrans(dict.fromkeys('-'))


def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    #record = homogenize_latex_encoding(record)
    record = type(record)
    record = page_double_hyphen(record)

    return record


with open(sys.argv[1], 'r') as bibfile:
    parser = BibTexParser()
    parser.ignore_nonstandard_types = False
    parser.customization = customizations

    bibtex_database = bibtexparser.load(bibfile, parser=parser)

ids = []
fixed_entries = []
for entry in bibtex_database.entries:
    #remove duplicates
    if not entry['ID'] in ids:
        ids.append(entry['ID'])
        #remove keys
        for key in REMOVE_KEYS:
            if key in entry:
                del entry[key]

        #convert month strings to integers
        if 'month' in entry and len(entry['month']) == 3:
            entry['month'] = str(month_table[entry['month']])

        #convert online refs from misc to online
        if 'keywords' in entry and 'online' in entry['keywords'].split(','):
            entry['ENTRYTYPE'] = 'online'

        #title case
        if 'title' in entry:
            entry['title'] = titlecase(entry['title'])

        # isbn format
        if 'isbn' in entry:
            entry['isbn'] = entry['isbn'].translate(REMOVE_DASH_FROM_ISBN)

        # issn format
        if 'issn' in entry:
            if len(entry['issn']) == 8:
                entry['issn'] = entry['issn'][:4] + '-' + entry['issn'][4:]

        fixed_entries.append(entry)

bibtex_database.entries = fixed_entries

with open(sys.argv[1], 'w') as bibfile:
    bibtexparser.dump(bibtex_database, bibfile)

