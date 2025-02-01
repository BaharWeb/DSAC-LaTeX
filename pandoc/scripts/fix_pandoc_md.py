# -*- coding: utf-8 -*-
import sys, re

markdown = ''

with open(sys.argv[1], 'r') as mdinfile:
    markdown = mdinfile.read()

    headings = re.compile(r'\n(#+)([!\w])')
    markdown = re.sub(headings, '\n\g<1> \g<2>', markdown)

    todos = re.compile(r'(?!\*)(\(?TODO:[A-Za-z_ :\?\/]+\)?)(?!\*)')
    multi_bold = re.compile(r'\*\*\*+')
    markdown = re.sub(todos, '**\g<1>**', markdown)
    markdown = re.sub(multi_bold, '**', markdown)

    wrong_blanks = re.compile('﻿')
    markdown = re.sub(wrong_blanks, '', markdown)

    #enumeration_starts = r'(^(?!-).+$)\n(^-)'
    #markdown = re.sub(enumeration_starts, '\g<1>\n\n\g<2>', markdown)

with open(sys.argv[2], 'w') as mdoutfile:
    mdoutfile.write(markdown)
