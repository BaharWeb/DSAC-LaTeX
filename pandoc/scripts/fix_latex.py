# -*- coding: utf-8 -*-
import fileinput
import sys

replacements = {
    '◐': '\LEFTcircle',
    '◯': '\Circle',
    '⬤': '\CIRCLE',
    u'\u200B': '',
    '\includegraphics{': '\includegraphics[width=0.99\\textwidth]{',
    '. ': '.\n',
    '\n\\cref': '\n\\Cref',
    '\\textbf{TODO': '\\todo{TODO',
}

def map_replace(string, replacement_map):
    for character in replacement_map:
        string = string.replace(character, replacement_map[character])
    return string

for line in fileinput.input(sys.argv[1], inplace=True):
    sys.stdout.write(map_replace(line, replacements))
