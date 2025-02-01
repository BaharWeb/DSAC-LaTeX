import json
from collections import Counter
from itertools import permutations
import bibtexparser
#import pybibtex

SKIPCHARS = ['{', '}', '\\', '\'', '"', '.']

author_counts = Counter()
first_author_counts = Counter()
link_counter = Counter()

def group(name, first_authors):
    return 1 if name in first_authors else 2

with open('/Users/sebastian/Dropbox/PhD/bib/all/all.bib') as bibfile:
    bib = bibtexparser.load(bibfile)

for item in bib.entries:
    authors = item['author']
    for c in SKIPCHARS:
        authors = authors.replace(c, '')
    #print(authors)
    authors = authors.split(' and ')
    #print(authors)
    first_author_counts[authors[0].strip()] += 1
    for author in authors:
        author_counts[author.strip()] += 1
    for pair in permutations(authors, 2):
        if pair[0] < pair[1]:
            key = pair[0] + '####' + pair[1]
        else:
            key = pair[1] + '####' + pair[0]
        link_counter[key] += 1

author_names = sorted(set([a for a in author_counts.keys()]))

#print(first_author_counts)
#print(author_counts)

nodes = []
for name in author_names:
    print(name)
    nodes.append({'name': name, 'group': group(name, first_author_counts), 'value': author_counts[name]})
print(nodes)

links = []
for key in link_counter:
    source = key.split('####')[0]
    target = key.split('####')[1]
    value = link_counter[key]
    links.append({'source': author_names.index(source), 'target': author_names.index(target), 'value': value})
print(links)

json_data = {"nodes": nodes, "links": links}

with open('sota_analysis.json', 'w') as json_out:
    json_out.write(json.dumps(json_data, indent=2))
    json_out.write('\n')



