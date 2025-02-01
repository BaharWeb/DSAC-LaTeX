import yaml
import sys

from collections import OrderedDict

with open(sys.argv[1], 'r') as infile:
	data = yaml.load(infile)
	abbreviations = OrderedDict(sorted(data.items(), key=lambda t: t[0]))

	for key in sorted([k for k in abbreviations]):
		print '%s : %s' % (key, abbreviations[key])

#with open(sys.argv[2], 'w') as outfile:
#	pass