# -*- coding: utf-8 -*-
import sys, re

markdown = ''

with open(sys.argv[1], 'r') as mdinfile:
    markdown = mdinfile.read()

    wrong_blanks = re.compile('﻿')
    markdown = re.sub(wrong_blanks, '', markdown)

    escaped_cites = re.compile(r'\\([\[|\]|\@])')
    markdown = re.sub(escaped_cites, '\g<1>', markdown)

with open(sys.argv[1], 'w') as mdoutfile:
    mdoutfile.write(markdown)
